#   Auther      : Heinz Samuelsson
#   Date        : 2013-06-12
#   File        : ex2.2.2.py
#   Reference   : Python Scripting for Computational Science, page 33 ff
#   Description : Do a mathematical operation on data in an infile and produce a result
#                 to an outfile.
#                 How to use: > python ex2.2.2 data1.txt res1.txt
#   Python ver  : 2.7.3 (gcc 4.6.3)

import sys
import math


# calculate y^5*e^-y if y >= 0
def myfunc(y):
    if y >= 0.0:
        return y**5*math.exp(-y)
    else:
        return 0.0


# try-except block for handling potential errors.
# Two strings are required.
try:
    infilename  = sys.argv[1]
    outfilename = sys.argv[2]
except:
    # The name of the script is stored in sys.argv[0].
    # The value for exit differs from 0 => signifies an error.
    print "Usage:",sys.argv[0],"<infile> <outfile>"
    sys.exit(1)

# open infile and outfile for read resp write.
ifile = open(infilename,'r')
ofile = open(outfilename,'w')


# infile format (data1.txt):
#    0.0 3.2
#    0.5 4.3
#    1.0 8.3333
#    2.5 -0.25

# read line by line of in file
for line in ifile:

    # split the string into x and y value and put it into a list
    # ['0.0', '3.2']
    # ['0.5', '4.3']
    # ['1.0', '8.3333']
    # ['2.5', '-0.25']
    pair = line.split()

    # need to convert the string into a float
    x = float(pair[0])
    y = float(pair[1])

    fy = myfunc(y)

    # write to a file
    # %g     => compact format
    # %12.5  => scientific format with 5 decimals, 12 characters width
    ofile.write('%g %12.5e\n' %(x,fy))

ifile.close(); ofile.close()

# Result
#    0  1.36775e+01
#    0.5  1.99469e+01
#    1  9.66004e+00
#    2.5  0.00000e+00

