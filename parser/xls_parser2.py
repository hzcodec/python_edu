# Auther      : Heinz Samuelsson
# Date        : 2014-06-09
# File        : xls_parser2.py
# Reference   : -
# Description : Parse an *.xls file and produce an output text file.
#
#               How to run the script
#                 > python xls_parser2.py <name_of_spreadsheet>
#               To produce a docstring html file:
#                 > pydoc -w xls_parser2
#
# Python ver : 2.7.3 (gcc 4.6.3)

import sys
import xlrd


class Workbook:

    """
      Workbook class is holding information about the spreadsheet.
      Its name, the sheet names.
      It can create a text file holding all registers with its offset address.
      The addresses are in both decimal and hexadecimal values.
    """

    def __init__(self,wb):

        try:
            self.workbook      = xlrd.open_workbook(wb)
            self.workbook_name = wb
        except IOError:
            print "Error: xls-file does not exist."
            sys.exit()

        # get sheet names in xls-file
        self.MemoryMap_sheet        = self.workbook.sheet_by_index(0)
        self.RegisterDatabase_sheet = self.workbook.sheet_by_index(1)
        self.GlobalConfig_sheet     = self.workbook.sheet_by_index(2)

        # get number of used rows in Register Database sheet
        self.no_of_rows = self.RegisterDatabase_sheet.nrows

        # open header file
        self.hdr = open('header.h','w')

	self.h_file_regname = [] # holds register names, used to generate header file
	self.h_file_hexaddr = [] # holds hex addresses, used to generate header file

	self.no_of_registers = 0 # counter value for the number of registers

    def print_workbook_info(self):
        """
          Print spreadsheet information.
        """

        print 40*'-'
        print '    Spreadsheet information'
        print 'Name        : ',self.workbook_name
	print ' '
	print 'Header file is created.'


    def print_registers(self):
        """
          Print out all registers extracted from the *.xls file.
        """

        # loop over the first row of all cells and print it out
        for i in range(2,self.no_of_rows-1):

            cell_type = self.RegisterDatabase_sheet.cell_type(i,0)

            # if cell type is empty then skip it
            if (cell_type == 0):
                pass # don't do anything
            else:
                reg_name    = self.RegisterDatabase_sheet.cell_value(i,0)
                addr_offset = int(self.RegisterDatabase_sheet.cell_value(i,2))
                loop_var    = int(self.RegisterDatabase_sheet.cell_value(i,3))

                self._expand_regname(reg_name,addr_offset,loop_var)


    def _expand_regname(self,name,offset,var):
        """
          Expand register name according to loop variable found in the *.xls sheet
          CRI_LH_CR_DA_LO_$k => CRI_LH_CR_DA_LO_0

	  Args:
            name:   name of register 
            offset: address offset value 
            var   : loop variable found in *.xls sheet.
        """

        if (var == 0):
            _hexaddress = str(hex(offset))
	    res = '{0:35} {1:10}'.format(name,offset)
 
	    # collect reg names, hex address for later use
	    self.h_file_regname.append(name)
	    self.h_file_hexaddr.append(_hexaddress)

        else:
            for addr in range(0,var):
                b          = name.find('$')
		_hexaddress = str(hex(offset+addr))
                res = '{0:35} {1:10}'.format((name[0:b]+ str(addr)),(offset+addr))

                # collect reg names, hex address for later use
	        self.h_file_regname.append(name[0:b]+str(addr))
	        self.h_file_hexaddr.append(_hexaddress)

        # fill every new block of name with a space after
	self.h_file_regname.append(' ')
	self.h_file_hexaddr.append(' ')


    def print_header_file(self):
	"""
	  Create a header file with defines, register name and its address.
	"""

        # make sure the name is always in uppercase
        self.hdr.write('#ifndef ' + self.workbook_name.upper() + '__' + '\n')
        self.hdr.write('#define ' + self.workbook_name.upper() + '__' + '\n')
        self.hdr.write('\n')

	length2 = len(self.h_file_regname)
	for i in range(0,length2):

            newstring =  '{0:35} {1:10}'.format(self.h_file_regname[i],self.h_file_hexaddr[i])
	     
            # if there is a space then just print a blank line otherwise print out the define
	    if not self.h_file_regname[i].isspace():
                self.hdr.write('#define ' + newstring + '\n')
		self.no_of_registers += 1
                sys.stdout.write('.') # a trick to omit the space after each character
	    else:
                self.hdr.write('\n')

        self.hdr.write('#endif\n')
	print '\n\n' + 'Number of created registers:',self.no_of_registers
        print 40*'-'


    def close_files(self):
	self.hdr.close()

 

def main():

    # first argument shall be the name of the xls-spreadsheet
    filename = sys.argv[1]

    workbook = Workbook(filename)
    workbook.print_workbook_info()
    workbook.print_registers()
    workbook.print_header_file()
    workbook.close_files()


if __name__ == '__main__':
    main()
