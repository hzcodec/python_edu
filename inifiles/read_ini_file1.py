# 
#   Auther      : Heinz Samuelsson
#   Date        : 2014-06-11
#   File        : read_ini_file1.py
#   Reference   : Beginning Python Visualization, p.125
#   Description : Read an ini-file and print out the contents.
#   Python ver  : 2.7.3 (gcc 4.6.3)

import ConfigParser

read_opts = ConfigParser.ConfigParser()
read_opts.read('options.ini')

for section in read_opts.sections():
    print "[%s]" % section
    for param in read_opts.items(section):
        print param
