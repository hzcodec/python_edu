# 
#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : argparse_test3.py
#   Reference   : http://docs.python.org/2/howto/argparse.html
#   Description : Test of argparse library.
#   Python ver  : 2.7.3 (gcc 4.6.3)


import argparse

parser = argparse.ArgumentParser()

# Optional argument.
parser.add_argument("--verbose", help="Increase output verbosity", action="store_true")
args = parser.parse_args()

if args.verbose:
    print "Verbosity turned on"

#
#  Result from run:
#

