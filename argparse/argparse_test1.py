# 
#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : argparse_test1.py
#   Reference   : http://docs.python.org/2/howto/argparse.html
#   Description : Test of argparse library.
#   Python ver  : 2.7.3 (gcc 4.6.3)


import argparse

parser = argparse.ArgumentParser()

# Positional argument, command-line option.
# Requires to specify an option.
parser.add_argument("par1", help="First parameter (is a string)")
args = parser.parse_args()

print args.par1


#
#  Result from run:
#      python argparse_test1.py testing
#      testing
#

