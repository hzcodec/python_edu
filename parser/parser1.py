# Auther      : Heinz Samuelsson
# Date        : 2014-06-09
# File        : parser1.py
# Reference   : www.decalage.info/python/configparser
# Description : Parse a file.
#
# Python ver : 2.7.3 (gcc 4.6.3)

COMMENT_CHAR = '#'
OPTION_CHAR =  '='


def parse_config(filename):

    # declare a dictionary
    options = {}
    f = open(filename)

    for line in f:

        # First, remove comments:
        if COMMENT_CHAR in line:
            # split on comment char, keep only the part before
            line, comment = line.split(COMMENT_CHAR, 1)

        # Second, find lines with an option=value:
        if OPTION_CHAR in line:
            # split on option char:
            option, value = line.split(OPTION_CHAR, 1)
            # strip spaces:
            option = option.strip()
            value = value.strip()
            # store in dictionary:
            options[option] = value

    f.close()
    return options


def main():

    options = parse_config('config.ini')
    print options

    # print out information from dictionary
    print 'Keys: ',options.keys()
    print 'Value:',options.values()
    print 'Length:',len(options)

    # print out values for the keys
    print 'Key - option3:',options['option3']
    print 'Key - option4:',options['option4']


if __name__ == '__main__':
    main()
