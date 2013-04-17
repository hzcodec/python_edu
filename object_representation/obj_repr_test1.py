#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : obj_repr_test1.py
#   Reference   : Python Essential Reference
#   Description : Test of __add__ and __str__ function.
#   Python ver  : 2.7.3 (gcc 4.6.3)

class Base:

    # constructor
    def __init__(self,n):
        print "__init__ called"
        self.a = n
        self.b = n*2


    # add self.a and self.b for the two objects
    # return value is a tuple
    def __add__(self,other):
        print "__add__ called"
        return self.a + other.a, self.b + other.b


    # print out attributes of an object
    def __str__(self):
        r = str(self.a)
        s = str(self.b)
        t = r+","+s
        return t


if __name__ == "__main__":

    base  = Base(10)
    base2 = Base(40)
    print 80*"-"

    # add 'a' and 'b' for the objects, __add__ is called
    x = base + base2
    print "x:",x
    print "x[0]:",x[0]
    print "x[1]:",x[1]

    # print out attribute, __str__ is called
    print "a,b:",base
    print "a,b:",base2


#  Result from run:
#   __init__ called
#   __init__ called
#   ----------------------------------------------------------
#   __add__ called
#   x: (50, 100)
#   x[0]: 50
#   x[1]: 100
#   a,b: 10,20
#   a,b: 40,80

