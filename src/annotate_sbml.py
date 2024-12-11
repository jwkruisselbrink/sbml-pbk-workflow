import os
import sys
import argparse
import traceback
import libsbml as ls
from pathlib import Path
from sbmlpbkutils import PbkModelAnnotator
from sbmlutils.log import get_logger

logger = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Annotate the SBML model file with the specifications of the annotations file.")
    parser.add_argument("sbml_file", help="Full path to SBML file")
    parser.add_argument("annotations_file", help="Full path to SBML file")
    parser.add_argument("out_file", help="Output file")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing")
    args = parser.parse_args()
    f_in = Path(args.sbml_file)
    f_ann = Path(args.annotations_file)
    f_out = Path(args.out_file)
    if not f_in.is_file():
        raise FileNotFoundError(f'SBML file [{f_in}] does not exist.')
    if not f_ann.is_file():
        raise FileNotFoundError(f'Annotations file [{f_ann}] does not exist.')
    try:
        if not f_out.exists() or args.force:
            
            # Check if output folder exists, otherwise create it
            out_dir = os.path.dirname(f_out)
            if not os.path.exists(out_dir):
                os.makedirs(out_dir)

            # Annotate SBML file
            annotator = PbkModelAnnotator()
            document = annotator.annotate(f_in, f_ann, logger)

            # Write SBML
            ls.writeSBML(document, str(f_out))
        else:
            print(f'[{f_out}] already exists, use -f to force conversion')
    except Exception as e:
        print(f'Unit annotation failed')
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
