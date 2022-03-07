import argparse
import os
from constants import DESCRIPTION, PROGRAM_SHORTCUT

# Functions
def length_value_limit(arg):
    # limits arguments to positive integers
    try:
        argument = int(arg)
    except ValueError:
        raise argparse.ArgumentTypeError("Must be an integer")
    if argument < 0:
        raise argparse.ArgumentTypeError("Argument must be positive")
    return argument


parser = argparse.ArgumentParser(prog=PROGRAM_SHORTCUT, description=DESCRIPTION)

# positional arguments
parser.add_argument("output_file", type=str, help="Specify output file name")

# optional arguments true/false
parser.add_argument("-f", "--filesonly", action="store_true", help="Returns only names of files")
parser.add_argument("-d", "--dirsonly", action="store_true", help="Returns only names of directorie")
parser.add_argument("-u", "--unique", action="store_true", help="Duplicit names are included only once (if combined with -e ignores file types)")
parser.add_argument("-e", "--extension", action="store_true", help="Include file extensions in filenames")

# optional arguments that require input
parser.add_argument("-L", "--length", type=length_value_limit, metavar="NUMBER", help="Specify depth of a search", default=0)
parser.add_argument("-D", "--directory", type=str, metavar="DIRECTORY", help="Specify target directory", default=os.getcwd())

# exclusive group -i (format via indentation) and -s (alphanumericall sort)
format_sort_group = parser.add_mutually_exclusive_group()
format_sort_group.add_argument("-i", "--indent", action="store_true", help="Returns formated list with indentation")
format_sort_group.add_argument("-s", "--sort", action="store_true", help="Returns alphanumerically sorted list")

# exclusive group -E (excluded extensions) and -I (included extensions)
ext_group = parser.add_mutually_exclusive_group()
ext_group.add_argument("-E", "--exclude", type=str, metavar="EXTENSIONS", help="Excludes specified file extensions - separate by \';\' [-E jpg;png]")
ext_group.add_argument("-I", "--include", type=str,metavar="EXTENSIONS", help="Includes only specified file extensions - separate by \';\' [-I jpg;png]")

args = parser.parse_args()