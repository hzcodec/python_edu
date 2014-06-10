# Auther      : Heinz Samuelsson
# Date        : 2014-06-09
# File        : xls_parser2.py
# Reference   : -
# Description : Parse an *.xls file and produce an output text file.
#
#               How to run the script
#                 > python xls_parser2.py <filename_of_xls_file>
#               To produce a docstring html file:
#                 > pydoc -w xls_parser
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

        # open out file
        self.outfile = open('register_file.txt','w')
        self.outfile.write('Register                                  Address' + '\n')

        # open header file
        self.hdr = open('header.h','w')

	self.h_file_regname = [] # holds register names, used to generate header file
	self.h_file_hexaddr = [] # holds hex addresses, used to generate header file


    def print_workbook_info(self):
        """
          Print spreadsheet information.
        """

        print 40*'-'
        print '    Spreadsheet information'
        print 'Name        : ',self.workbook_name
        print 'Sheet name 1: ',self.MemoryMap_sheet.name
        print 'Sheet name 2: ',self.RegisterDatabase_sheet.name
        print 'Sheet name 3: ',self.GlobalConfig_sheet.name

        print 40*'-'


    def print_registers(self,expanded=False):
        """
          Print out all registers extracted from the *.xls file.

	  Args:
	    expanded: True/False - Default = False. If True then registers
	              are expanded.
        """

        print 'Register                                offset address'

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

                # if expanded selected then print out expanded names and addresses
		if (expanded):
                    self._expand_regname(reg_name,addr_offset,loop_var)
		else:
         	    print '{0:35} - {1:10d}'.format(reg_name,addr_offset)


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
            hexaddress = str(hex(offset))
	    res = '{0:35} {1:10}'.format(name,offset)
	    print res
            self.outfile.write(res + '      ' + hexaddress + '\n')
 
	    # collect reg names, hex address for later use
	    self.h_file_regname.append(name)
	    self.h_file_hexaddr.append(hexaddress)
            

        else:
            for addr in range(0,var):
                b          = name.find('$')
		hexaddress = str(hex(offset+addr))
                res = '{0:35} {1:10}'.format((name[0:b]+ str(addr)),(offset+addr))
                print res

                # print to outfile
                self.outfile.write(res + '      ' + hexaddress + '\n')
	        
                # collect reg names, hex address for later use
	        self.h_file_regname.append(name[0:b]+str(addr))
	        self.h_file_hexaddr.append(hexaddress)

        print ''
        self.outfile.write('\n')


    def print_header_file(self):

        # make sure the name is always in uppercase
        self.hdr.write('#ifndef ' + self.workbook_name.upper() + '__' + '\n')
        self.hdr.write('#define ' + self.workbook_name.upper() + '__' + '\n')
        self.hdr.write('\n')

	length2 = len(self.h_file_regname)
	for i in range(0,length2):
            newstring =  '{0:35} {1:10}'.format(self.h_file_regname[i],self.h_file_hexaddr[i])
            self.hdr.write('#define ' + newstring + '\n')

        self.hdr.write('\n#endif\n')



    def close_files(self):
	self.outfile.close()
	self.hdr.close()

 

def main():

    # first argument shall be the input filename
    filename = sys.argv[1]

    workbook = Workbook(filename)
    workbook.print_workbook_info()
    workbook.print_registers(True)
    workbook.print_header_file()
    workbook.close_files()


if __name__ == '__main__':
    main()
