"""
    An example on how to use 'argparse' to parse arguments from command line.
    Useful article: https://docs.python.org/3/howto/argparse.html
"""
import argparse

# Parse all arguments
parser = argparse.ArgumentParser()
# Restrict arguments so they can't be entered together
group = parser.add_mutually_exclusive_group()

# Optional arguments
parser.add_argument("-r", "--random", action="store_true",
                    help="a random flag")
group.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true",
                    help="simplest output")

# Positional arguments: required arguments
parser.add_argument("number", type=int, help="Enter a number")

# Parse the arguments
args = parser.parse_args()

if args.quiet:
    print args.number
elif args.verbose:
    print "You entered:", args.number
else:
    print "Number:", args.number

