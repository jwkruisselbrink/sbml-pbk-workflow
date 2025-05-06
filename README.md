# SBML PBK workflow

[GitHub workflow](https://docs.github.com/en/actions/using-workflows) for automated generation of annotated SBML files from Antimony PBK model implementations combined with annotations provided in CSV file annotations. The workflow contains the following main build steps for creation and annotation of the SBML file:

1. Create SBML file from Antimony model implementation.
2. Annotate the SBML file with units and terms, based on the annotations CSV file.
3. Validate the SBML file for completeness and consistency of units.
4. Store the generated SBML file and log files in the build artifacts.
5. Add the generated SBML file to the repository.

## Usage

Adding the SBML PBK workflow to your GitHub repository requires the following steps:

1. The Antimony model implementation should be placed in a subfolder *model/* in the repository. In this folder, both the Antimony model implementation and the annotations CSV file should be placed. The annotations file should have the same file base name as the Antimony file, but with extension *.annotations.csv*. The repository should have the two files *model/[MODEL_NAME].ant* and *model/[MODEL_NAME].annotations.csv*

2. Set the contents-permission of the default GITHUB_TOKEN to true. This is required for pushing new commits to the repository.

3. Create a file named 'build.yml' in the `.gihub/workflows` folder 

```yaml
name: Build
on: [push, workflow_dispatch]

jobs:
  create-and-annotate-sbml:
    uses: jwkruisselbrink/sbml-pbk-workflow/.github/workflows/build.yml@v8
    with:
      model-name: [MODEL_NAME]
    permissions:
      contents: write
    secrets: inherit
```

4. Optionally, you can also create a separate validate step (executed after successful run of the build workflow). To do so, create a file named 'validate.yml' in the `.gihub/workflows` folder 

```yaml
name: Validate
on:
  workflow_run:
    workflows: ["Build"]
    types: [completed]
jobs:
  validate-sbml:
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    uses: jwkruisselbrink/sbml-pbk-workflow/.github/workflows/validate.yml@v8
    with:
      model-name: [MODEL_NAME]
    secrets: inherit
```

## Workflow build steps

### SBML conversion

The python script [ant2sbml.py](src/ant2sbml.py) is used to automatically create an SBML file from the Antimony file. For this, it uses the Python [Tellurium](https://tellurium.analogmachine.org/) package.

### SBML model annotation

In the model annotation step, the generated SBML file is annotated using the terms and units specified in a CSV file. The [model annotation script](src/annotate_sbml.py) uses methods of the experimental [SBML-PBK-utils](https://github.com/jwkruisselbrink/sbml-pbk-utils) packages.

For information on formatting the annotations file, consult the documentation of the [SBML-PBK-utils](https://github.com/jwkruisselbrink/sbml-pbk-utils) packages. For an example of an annotations file, see the [annotations file](https://github.com/rivm-syso/euromix-to-sbml/blob/main/model/euromix.annotations.csv) of the SBML EuroMix PBK model re-implementation.

### SBML validation

Automatic validation can be included to check for model errors, model consistency, consitency of units, and also on more PBK-model specific aspects. The script [validate_sbml.py](src/validate_sbml.py) runs validation checks on the SBML file. This is a first version in which some rudimentary file and consistency checks are performed.
