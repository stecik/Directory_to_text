import argparse
from constants import DESCRIPTION, SWITCHES

parser = argparse.ArgumentParser(description=DESCRIPTION)
# parser.add_argument("switches", type=str, metavar="", help=SWITCHES)
parser.add_argument("-f", "--filesonly", action="store_true", help="Return only names of files")
parser.add_argument("-d", "--dirsonly", action="store_true", help="Return only names of directorie")
parser.add_argument("-u", "--unique", action="store_true", help="Duplicit names are included only once (if combined with -e ignores file types)")
parser.add_argument("-e", "--extension", action="store_true", help="Include file extensions in filenames")

format_sort_group = parser.add_mutually_exclusive_group()
format_sort_group.add_argument("-i", "--indent", action="store_true", help="Return formated list with indentation")
format_sort_group.add_argument("-s", "--sort", action="store_true", help="Return alphanumerically sorted list (if combined with -i, -a is ignored)")

ext_group = parser.add_mutually_exclusive_group()
ext_group.add_argument("-E", "--exclude", type=str, help="Excludes specified file extensions - separate by \';\' [-E jpg;png]")
ext_group.add_argument("-I", "--include", type=str, help="Includes only specified file extensions - separate by \';\' [-I jpg;png]")

ext_group.add_argument("-D", "--depth", type=int, help="Specify depth of a search", default=0)

args = parser.parse_args()