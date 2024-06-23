import sys
import argparse
import libsbml as ls
from pathlib import Path
import traceback
import pandas as pd
from unit_definitions import UnitDefinitions
from term_definitions import TermDefinitions

def main():
    """Creates an annotation template for the provided SBML file."""
    parser = argparse.ArgumentParser(description="Create a CSV file of the terms of an SBML model.")
    parser.add_argument("sbml_file", help="Full path to the SBML file")
    parser.add_argument("-o", "--out", required=False, help="Output file")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing")
    args = parser.parse_args()
    f_in = Path(args.sbml_file)
    if not f_in.is_file():
        raise FileNotFoundError(f'File {f_in} does not exist.')
    if args.out:
        f_out = Path(args.out)
    else:
        f_out = Path(args.sbml_file).with_suffix('.csv')

    try:
        # Load the document
        document = ls.readSBML(f_in)
        # Get the model
        model = document.getModel()
    except Exception as e:
        print(f'Could not load SBML file {f_in}')
        traceback.print_exc()
        sys.exit(1)

    # Create terms datatable
    df = exportTerms(model)

    # Write data table to csv file
    if not f_out.exists() or args.force:
        df.to_csv(f_out, index=False)
        print(f'{f_in} converted to {f_out}')
    else:
        print(f'{f_out} already exists, use -f to force conversion')

def getUnitString(element):
    """Tries to get the (UCUM formated) unit string of the specified element."""
    unit = ls.UnitDefinition.printUnits(element.getDerivedUnitDefinition())
    unit = element.getUnits()
    if (unit):
        for index, value in enumerate(UnitDefinitions):
            if unit.lower() == value['id'].lower() \
                or any(val.lower() == unit.lower() for val in value['common_ids']):
                return value['UCUM'] if value['UCUM'] else value['id']
    return ""

def getResourceDefinition(element, element_type):
    """Tries to find a resource definition for the specified element."""
    element_id = element.getId()
    for index, value in enumerate(TermDefinitions):
        if value['element_type'] == element_type:
            if 'recommended_id' in value.keys() \
                and element_id.lower() == value['recommended_id'].lower():
                return value
            elif 'common_ids' in value.keys() \
                and any(element_id.lower() == val.lower() for val in value['common_ids']):
                return value
    return None

def getTerm(element):
    """Helper function to extract is-a resource URI."""
    cvTerms = element.getCVTerms()
    if cvTerms:
        # Check if there already is an annotation for the element
        for term in cvTerms:
            num_resources = term.getNumResources()
            for j in range(num_resources):
                if term.getQualifierType() == ls.BIOLOGICAL_QUALIFIER and \
                    term.getBiologicalQualifierType() == ls.BQB_IS:
                    return term.getResourceURI(j)

    return None 

def exportTerms(model):
    dt = []
    dt_compartments = getCompartmentTerms(model)
    dt.extend(dt_compartments)
    dt_species = getSpeciesTerms(model)
    dt.extend(dt_species)
    dt_parameters = getParameterTerms(model)
    dt.extend(dt_parameters)
    terms = pd.DataFrame(
        dt,
        columns=["element_id", "sbml_type", "element_description", "unit", "URI", "description", "remark"]
    )
    return terms

def getCompartmentTerms(model):
    element_type="compartment"
    dt = []
    for i in range(0,model.getNumCompartments()):
        element = model.getCompartment(i)

        name = element.getName()
        description = ''
        uri = getTerm(element)

        # Try to find resource definition for element
        resource = getResourceDefinition(element, element_type)
        if (resource is not None):
            if 'resources' in resource.keys():
                uri = resource['resources'][0]['URI']
            if 'name' in resource.keys():
                name = resource['name']
            if 'description' in resource.keys():
                description = resource['description']

        dt.append([
            element.getId(),
            element_type,
            name,
            getUnitString(element),
            uri,
            description,
            ""
        ])
    return dt

def getSpeciesTerms(model):
    element_type="species"
    dt = []
    for i in range(0,model.getNumSpecies()):
        element = model.getSpecies(i)

        name = element.getName()
        description = ''
        uri = getTerm(element)

        # Try to find resource definition for element
        resource = getResourceDefinition(element, element_type)
        if (resource is not None):
            if 'resources' in resource.keys():
                uri = resource['resources'][0]['URI']
            if 'name' in resource.keys():
                name = resource['name']
            if 'description' in resource.keys():
                description = resource['description']

        dt.append([
            element.getId(),
            element_type,
            name,
            getUnitString(element),
            uri,
            description,
            ""
        ])
    return dt

def getParameterTerms(model):
    element_type="parameter"
    dt = []
    for i in range(0,model.getNumParameters()):
        element = model.getParameter(i)

        name = element.getName()
        description = ''
        uri = getTerm(element)

        # Try to find resource definition for element
        resource = getResourceDefinition(element, element_type)
        if (resource is not None):
            if 'resources' in resource.keys():
                uri = resource['resources'][0]['URI']
            if 'name' in resource.keys():
                name = resource['name']
            if 'description' in resource.keys():
                description = resource['description']

        dt.append([
            element.getId(),
            element_type,
            name,
            getUnitString(element),
            uri,
            description,
            ""
        ])
    return dt

if __name__ == "__main__":
    main()
