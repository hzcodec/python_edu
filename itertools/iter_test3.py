#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-29
#   File        : iter_test3.py
#   Reference   : -
#   Description : Test of itertools. Print out permutations.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import itertools

a = list(itertools.product(['1','X','2'],repeat=2))

list_len = len(a)

for i in range(0,list_len):
    if (i < 9):
        print i+1,' ',a[i]
    else:
        print i+1,'',a[i]

print ''

# Result:
#
#   1   ('1', '1')
#   2   ('1', 'X')
#   3   ('1', '2')
#   4   ('X', '1')
#   5   ('X', 'X')
#   6   ('X', '2')
#   7   ('2', '1')
#   8   ('2', 'X')
#   9   ('2', '2')
