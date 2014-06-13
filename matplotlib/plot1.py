#   Auther      : Heinz Samuelsson
#   Date        : 2014-06-11
#   File        : plot1.py
#   Reference   : -
#   Description : Simple example, with headline, x-and y-axis are named.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import matplotlib.pyplot as plt

plt.title('Headline')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.plot([1,2,3,4])

plt.show()
