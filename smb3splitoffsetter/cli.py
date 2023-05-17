import argparse

from smb3splitoffsetter.main import main
from smb3splitoffsetter.models import OffsetTypes


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="smb3-split-offsetter",
        description="Offset smb3 warpless splits by about 17s/31s each world to accomodate offscreen wand grabs.",
        epilog="usage: offsetsplits.py lss_file lss_file_out peach",
    )
    parser.add_argument("infile")
    parser.add_argument("outfile")
    parser.add_argument("type", choices=[e.name.lower() for e in OffsetTypes])
    args = parser.parse_args()
    main(args.infile, args.outfile, args.type)
