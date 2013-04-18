#   Auther      : Heinz Samuelsson
#   Date        : 2013-04-16
#   File        : raw_input_test2.py
#   Reference   : - 
#   Description : Test of user input from the keyboard. The input shall be an int.
#                 If incorrect value is entered an exception is raised.
#   Python ver  : 2.7.3 (gcc 4.6.3)

x = raw_input("Enter a number ")

try:
    y = 99 + int(x)
    print "Your number is:",y
except ValueError:
    print "Error! You did'nt enter a number."

