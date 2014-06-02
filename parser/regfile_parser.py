#   Auther      : Heinz Samuelsson
#   Date        : 2014-05-31
#   File        : regfile_parser.py
#   Reference   : -
#   Description : Parse a register file and produce a C-header file.
#                 To see an example of an input file see regfile.txt.
#
#   Python ver  : 2.7.3 (gcc 4.6.3)

f = open('regfile.txt','r')
g = open('outfile.h','w')

lines = f.read().splitlines()

current_row            = 0
row_blockname          = []
row_registername       = []
register_found         = 0
last_char_pos_reg_name = 28 # last character position for registername
start_pos_reg_addr     = 29 # start position for register address
start_pos_comment      = 51 # start position for comment of register
stop_pos_comment       = 85 # stop position for comment of register


# find empty lines and startpos for blockname/registername
for line in lines:
    
    # if register found then continue until blank row
    if register_found:

        if not line:
            register_found = 0

        else:
            print '0:25 :',line[0:last_char_pos_reg_name]
            print 'start :',line[start_pos_reg_addr:start_pos_reg_addr+10]

            # add block address and local register address
            x = int(line[start_pos_reg_addr:start_pos_reg_addr+10],16) + int(lines[current_blockname_row+1][start_pos_reg_addr:start_pos_reg_addr+10],16)
            print 'Address:',hex(x)
            g.write('#define   '+line[0:25] + hex(x) + '   //' + line[start_pos_comment:stop_pos_comment] + '\n')

    elif 'blockname' in line:
        row_blockname.append(current_row)
        current_blockname_row = current_row

    elif 'registername' in line:
        row_registername.append(current_row)
        register_found = 1
        print lines[current_blockname_row+1]
        
    current_row += 1


print 10*'-'
print 'blockname at:',row_blockname
print "registernames at:",row_registername
print 10*'-'

f.close()
g.close()

