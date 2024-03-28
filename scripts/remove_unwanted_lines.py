from argparse import ArgumentParser
import re


argparse = ArgumentParser()
argparse.add_argument(
    "-i",
    "--input_file",
    help="Path to the input file where all the raw reads are stored (must be fasta)",
    required=True,
)

args = argparse.parse_args()


inf = args.input_file

import re

def check_string(s):
    pattern = r'^T\d{3},\d\.0\n$'
    return bool(re.match(pattern, s))

if __name__=="__main__":
    c = open(inf, "r+")
    lines = c.readlines()
    c.seek(0)
    c.truncate()
    for line in lines:
        if check_string(line) or line=="Id,Predicted\n":
            c.write(line)
        else:
            continue
    # for line in lines:
    #     if line.endswith("1.0\n"):
    #         c.write(line[:-4]+"0.0\n")
    #     else:
    #         c.write(line[:-4]+"1.0\n")
    # c.close()



