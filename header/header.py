#   File             : header.py
#   Version          : 1.0
#   Date             : 2014-05-09
#   Author           : Heinz Samuelsson
#   Reference        : http://code.activestate.com/recipes/'
#                             577846-python-script-to-create-a-header-for-python-script/
#   Description      : Create a header for Python scripts.
#   python_versiont  : 2.7.3 (gcc 4.6.3)
#========================================================================


# Import the modules needed to run the script.
from os.path import exists
from time import strftime
import os

title = raw_input("Enter a file name for your script: ")

# Add .py to the end of the script.
title = title + '.py'

# Convert all letters to lower case.
title = title.lower()

# Remove spaces from the title.
title = title.replace(' ', '_')

# Check to see if the file exists to not overwrite it.
if exists(title):
    print "\nA script with this name already exists."
    exit(1)

descrpt = raw_input("Enter a description: ")
name    = raw_input("Enter your name: ")
ver     = raw_input("Enter the version number: ")
ref     = raw_input("Enter the reference (URL name) : ")
div     = '================================'

# Create a file that can be written to.
filename = open(title, 'w')

# Set the date automatically.
date = strftime("%Y-%m-%d")

# Write the data to the file.
filename.write('#!/usr/bin/python')
filename.write('\n#   File             : ' + title)
filename.write('\n#   Version          : ' + ver)
filename.write('\n#   Date             : ' + date)
filename.write('\n#   Author           : ' + name)
filename.write('\n#   Reference        : ' + ref)
filename.write('\n#   Description      : ' + descrpt)
filename.write('\n#   python_version   : 2.7.3 (gcc 4.6.3)')
filename.write('\n#' + div*2 + '\n')
filename.write('\n')
filename.write('\n')

# Close the file after writing to it.
filename.close()

# Clear the screen. This line of code will not work on Windows.
os.system("clear")


def select_editor():
    '''Open the file with either the Vim or Emacs editor.'''
    os.system("vim +12 " + title)
    exit()

#select_editor()

