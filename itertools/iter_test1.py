#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-29
#   File        : iter_test1.py
#   Reference   : -
#   Description : Test of itertools. Generate a binare sequence.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import itertools

for x in itertools.product('01',repeat=4):
    print ''.join(x)

# Result:
#   0000
#   0001
#   0010
#   0011
#   0100
#   0101
#   0110
#   0111
#   1000
#   1001
#   1010
#   1011
#   1100
#   1101
#   1110
#   1111

