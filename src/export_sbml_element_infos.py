import sys
import argparse
import libsbml as ls
from pathlib import Path
import traceback
from sbml_element_infos_exporter import sbmlElementInfosExporter

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
    infosExporter = sbmlElementInfosExporter()
    df = infosExporter.exportTerms(model)

    # Write data table to csv file
    if not f_out.exists() or args.force:
        df.to_csv(f_out, index=False)
        print(f'{f_in} converted to {f_out}')
    else:
        print(f'{f_out} already exists, use -f to force conversion')


if __name__ == "__main__":
    main()
