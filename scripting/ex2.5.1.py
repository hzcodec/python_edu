#   Auther      : Heinz Samuelsson
#   Date        : 2013-06-14
#   File        : ex2.5.1.py
#   Reference   : Python Scripting for Computational Science, page 66 ff
#   Description : Read in a file and create new files.
#                 How to use: > python ex2.2.2 data1.txt res1.txt
#   Python ver  : 2.7.3 (gcc 4.6.3)

import sys
import math
import string

usage = 'Usage: %s <infile>'% sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print usage
    sys.exit(1)

ifile = open(infilename,'r')

# read first comment line
line = ifile.readline()
print line

# read next line, contains the increment value
dt = float(ifile.readline())
print dt

# read headlines and put them in a list
ynames = ifile.readline().split()
# ['measurements', 'model1', 'model2']
print ynames

outfiles = []
for name in ynames:
    outfiles.append(open(name+'.dat','w'))

t = 0.0

for line in ifile:
    yvalues = line.split()
    if len(yvalues) == 0:
        continue
    
    for i in range(len(outfiles)):
        outfiles[i].write('%12g %12.5e\n' % (t,float(yvalues[i])))

    t += dt

for file in outfiles:
    file.close()

