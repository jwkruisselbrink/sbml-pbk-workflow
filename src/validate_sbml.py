import argparse
import logging
import sys
from pathlib import Path
from sbmlpbkutils import PbkModelValidator
from sbmlutils.log import get_logger

def create_file_logger(
    logfile: str
) -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(logfile, 'w+')
    formatter = logging.Formatter('[%(levelname)s] - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

def main():
    """usage: validate_sbml.py inputfile logfile
    """
    parser = argparse.ArgumentParser(description="Validate SBML file")
    parser.add_argument("f_in", help="Path to the SBML file")
    parser.add_argument("log_file", help="Path to log file")
    args = parser.parse_args()
    f_in = Path(args.f_in)
    if not f_in.is_file():
        raise FileNotFoundError(f'File {f_in} does not exist.')
    logger = get_logger(__name__) if args.log_file is None else create_file_logger(Path(args.log_file))

    validator = PbkModelValidator()
    validator.validate(f_in, logger)

if __name__ == '__main__':
  main(sys.argv) 
