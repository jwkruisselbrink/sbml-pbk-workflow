
#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )

python "$parent_path"/src/ant2sbml.py model/$1.ant -f

python "$parent_path"/src/annotate_sbml_terms.py model/$1.sbml model/$1.terms.csv model/$1.sbml

python "$parent_path"/src/annotate_sbml_units.py model/$1.sbml model/$1.units.csv model/$1.sbml -f

python "$parent_path"/src/validate_sbml.py model/$1.sbml
