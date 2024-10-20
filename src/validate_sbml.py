import sys
import argparse
from pathlib import Path
from sbmlpbkutils import PbkModelValidator
from sbmlutils.log import get_logger

logger = get_logger(__name__)

def main (args):
    """usage: validateSBML.py inputfile
    -u  skips unit consistency check
    """
    parser = argparse.ArgumentParser(description="Validate SBML file")
    parser.add_argument("f_in", help="Path to the SBML file")
    args = parser.parse_args()
    f_in = Path(args.f_in)
    if not f_in.is_file():
        raise FileNotFoundError(f'File {f_in} does not exist.')

    validator = PbkModelValidator()
    validator.validate(f_in, logger)

if __name__ == '__main__':
  main(sys.argv) 
