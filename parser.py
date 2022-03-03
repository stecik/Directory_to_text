import argparse
import os
from constants import DESCRIPTION

parser = argparse.ArgumentParser(description=DESCRIPTION)

parser.add_argument("output_file", type=str, help="Specify output file name")
parser.add_argument("-D", "--directory", type=str, metavar="", help="Specify target directory", default=os.getcwd())
parser.add_argument("-f", "--filesonly", action="store_true", help="Returns only names of files")
parser.add_argument("-d", "--dirsonly", action="store_true", help="Returns only names of directorie")
parser.add_argument("-u", "--unique", action="store_true", help="Duplicit names are included only once (if combined with -e ignores file types)")
parser.add_argument("-e", "--extension", action="store_true", help="Include file extensions in filenames")

parser.add_argument("-L", "--length", type=int, metavar="", help="Specify depth of a search", default=0)

format_sort_group = parser.add_mutually_exclusive_group()
format_sort_group.add_argument("-i", "--indent", action="store_true", help="Returns formated list with indentation")
format_sort_group.add_argument("-s", "--sort", action="store_true", help="Returns alphanumerically sorted list")

ext_group = parser.add_mutually_exclusive_group()
ext_group.add_argument("-E", "--exclude", type=str, help="Excludes specified file extensions - separate by \';\' [-E jpg;png]")
ext_group.add_argument("-I", "--include", type=str, help="Includes only specified file extensions - separate by \';\' [-I jpg;png]")

args = parser.parse_args()