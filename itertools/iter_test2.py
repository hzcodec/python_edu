#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-29
#   File        : iter_test2.py
#   Reference   : -
#   Description : Test of itertools.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import itertools

print list(itertools.product([0,1],repeat=4))

# Result:

#[(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]

