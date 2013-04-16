# 
#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : argparse_test3.py
#   Reference   : http://docs.python.org/2/howto/argparse.html
#   Description : Test of argparse library.
#   Python ver  : 2.7.3 (gcc 4.6.3)


import argparse

def f1():
    print "f1() called"


parser = argparse.ArgumentParser()

# Optional argument.
parser.add_argument("-v","--verbose", help="Increase output verbosity", action="store_true")
parser.add_argument("-t","--test", help="Testing", action="store_true")
args = parser.parse_args()

if args.verbose:
    print "Verbosity turned on"
elif args.test:
    f1()

#
#  Result from run:
#

