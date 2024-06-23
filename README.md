# SBML PBK workflow

GitHub workflow for creation of annotated SBML files from Antimony PBK model implementations combined with annotations provided in CSV file annotations.

## Usage

Adding the SBML PBK workflow to your GitHub repository requires the following steps:

1. The Antimony model implementation should be placed in a subfolder *model/* in the repository. In this folder, both the Antimony model implementation and the annotations CSV file should be placed. The annotations file should have the same file base name as the Antimony file, but with extension *.annotations.csv*. The repository should have the two files *model/[MODEL_NAME].ant* and *model/[MODEL_NAME].annotations.csv*

2. Set the contents-permission of the default GITHUB_TOKEN to true. This is required for pushing new commits to the repository.

3. Create a file named 'build.yml' in the `.gihub/workflows` folder 

```yaml
name: Create and annotate SBML
on: [push, workflow_dispatch]

jobs:
  create-and-annotate-sbml:
    uses: jwkruisselbrink/sbml-pbk-workflow/.github/workflows/build.yml@main
    with:
      model-name: [MODEL_NAME]
    permissions:
      contents: write
    secrets: inherit
```

## Build steps of the workflow

Besides some administrative steps, the workflow contains the following main build steps for creation and annotation of the SBML file. 

1. Create SBML file from Antimony model implementation.
2. Annotate the SBML file with units and terms, based on the annotations CSV file.
3. Validate the SBML file for completeness and consistency of units.
4. Store the generated SBML file and log files in the build artifacts.
5. Add the generated SBML file to the repository.

## SBML model annotation

In the model annotation step, the generated SBML file is annotated using the terms and units specified in a CSV file. The model annotation script is based on, and uses parts of, the annotation script of [SBMLutils](https://sbmlutils.readthedocs.io/en/latest/notebooks/sbml_annotator.html#Annotate-existing-model). However, in addition to annotation of the model using RDF triples, it also sets the model units and element names. The structure of the CSV file is also based on the external annotations file format of [SBMLutils](https://sbmlutils.readthedocs.io/en/latest/notebooks/sbml_annotator.html#Annotate-existing-model), but again with some changes to also allow for annotation of units.

| Field           | Description                                              |
|-----------------|----------------------------------------------------------|
| element_id      | Identifier of the model element that is to be annotated. |
| sbml_type       | Type of the model element that is to be annotated. Options: `model`, `document`, `compartment`, `species`, `parameter`. |
| element_name    | For specification of element name: the name of the model element. |
| unit            | For unit annotation: the unit associated with the model element. Specieid units should be compliant with the synonyms of the [unit definitions](src/unit_definitions.py). |
| annotation_type | For RDF annotation: type of the SBML term-annotation (default RDF). |
| qualifier       | For RDF annotation: [BioModels Qualifier](https://github.com/combine-org/combine-specifications/blob/main/specifications/qualifiers-1.1.md#model-qualifiers) of the annotation (RDF predicate). Model qualifier types: `BQM_IS`, `BQM_IS_DESCRIBED_BY`, `BQM_IS_DERIVED_FROM`, `BQM_IS_INSTANCE_OF`, `BQM_HAS_INSTANCE`. Biological qualifier types: `BQB_IS`, `BQB_HAS_PART`, `BQB_IS_PART_OF`, `BQB_IS_VERSION_OF`, `BQB_HAS_VERSION`, `BQB_IS_HOMOLOG_TO`, `BQB_IS_DESCRIBED_BY`, `BQB_IS_ENCODED_BY`, `BQB_ENCODES`, `BQB_OCCURS_IN`, `BQB_HAS_PROPERTY`, `BQB_IS_PROPERTY_OF`, `BQB_HAS_TAXON`. |
| URI             | For RDF annotation: annotation resource URI for the term-annotation (RDF object).  |

For specification of the SBML model global substance unit, time unit, and volume unit, use **element_id** values of *substanceUnits*, *timeUnits*, and *volumeUnits* with **sbml_type** *document*.

For an example of an annotations file, see the [annotations file](https://github.com/rivm-syso/euromix-to-sbml/blob/main/model/euromix.annotations.csv) of the SBML EuroMix PBK model re-implementation.