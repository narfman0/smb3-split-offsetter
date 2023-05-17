import sys


def get_in_out_files():
    help_args = ["-h", "--h", "-help", "--help", "-?", "--?"]
    if (len(sys.argv) == 2 and sys.argv[1] in help_args) or len(sys.argv) > 3:
        print("usage: offsetsplits.py lss_file [output]")
        exit()

    if len(sys.argv) == 1:
        infile = input("Enter splits file name: ")
    else:
        infile = sys.argv[1]

    if len(sys.argv) == 3:
        outfile = sys.argv[2]
    elif "." in infile:
        outfile = ".".join(infile.split(".")[:-1]) + "_out." + infile.split(".")[-1]
    else:
        outfile = infile + "_out"
    return infile, outfile
