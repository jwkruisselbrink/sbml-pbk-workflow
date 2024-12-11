import sys
import os
import argparse
import tellurium as te
import traceback
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Convert Antimony file to SBML")
    parser.add_argument("ant_file", help="Full path to Antimony file")
    parser.add_argument("out_file", help="Output file")
    parser.add_argument("-f", "--force", action="store_true", help="Overwrite existing")
    args = parser.parse_args()
    f_in = Path(args.ant_file)
    if not f_in.is_file():
        raise FileNotFoundError(f'File {f_in} does not exist.')
    try:
        r = te.loada(args.ant_file)
    except Exception as e:
        print(f'Tellurium could not process {f_in}')
        traceback.print_exc()
        sys.exit(1)

    # Get output file from command line args, otherwise derive from antimony file
    f_out = Path(args.out_file) if args.out_file is not None else Path(args.ant_file).with_suffix('.sbml')

    # Check if output folder exists, otherwise create it
    out_dir = os.path.dirname(f_out)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Export to SBML file
    if not f_out.exists() or args.force:
        r.exportToSBML(f_out)
        print(f'{f_in} converted to {f_out}')
    else:
        print(f'{f_out} exists, use -f to force conversion')

if __name__ == "__main__":
    main()
