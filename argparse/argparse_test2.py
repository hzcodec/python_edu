# 
#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : argparse_test2.py
#   Reference   : http://docs.python.org/2/howto/argparse.html
#   Description : Test of argparse library.
#   Python ver  : 2.7.3 (gcc 4.6.3)


import argparse

parser = argparse.ArgumentParser()

# Positional argument, command-line option.
# Requires to specify an option.
# Need to add type=int since input parameter shall be an integer
parser.add_argument("par1", help="First parameter (is a string)",type=int)
args = parser.parse_args()

print args.par1**2


#
#  Result from run:
#      python argparse_test1.py testing
#      testing
#

