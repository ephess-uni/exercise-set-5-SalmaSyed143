"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

import argparse
def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":

    argument_object = argparse.ArgumentParser(description="This program prints the number of lines in infile.")
    
    argument_object.add_argument("infile", type=argparse.FileType('r'))
    
    r = argument_object.parse_args()

    if r.infile:
        line_count(r.infile.name)
