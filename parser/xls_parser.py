import sys
import xlrd


class Workbook:

    def __init__(self,wb):

        self.workbook      = xlrd.open_workbook(wb)
        self.workbook_name = wb

        # get sheet names in xls-file
        self.MemoryMap_sheet        = self.workbook.sheet_by_index(0)
        self.RegisterDatabase_sheet = self.workbook.sheet_by_index(1)
        self.GlobalConfig_sheet     = self.workbook.sheet_by_index(2)

        # get number of used rows in Register Database sheet
        self.no_of_rows = self.RegisterDatabase_sheet.nrows


    """
      print workbook information
    """
    def print_workbook_info(self):

        print 40*'-'
        print '    Workbook information'
        print 'Spreadsheet name:',self.workbook_name
        print 'Sheet name 1:',self.MemoryMap_sheet.name
        print 'Sheet name 2:',self.RegisterDatabase_sheet.name
        print 'Sheet name 3:',self.GlobalConfig_sheet.name

        print 'Number of rows:',self.no_of_rows
        print 40*'-'

    """
      print out registers
      [in]   expanded    Expand register names
    """
    def print_registers(self,expanded=False):

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
                    self.expand_regname(reg_name,addr_offset,loop_var)
		else:
         	    print '{0:35} - {1:10d}'.format(reg_name,addr_offset)


    """
      expand register name according to loop variable found in the *.xls sheet
      CRI_LH_CR_DA_LO_$k => CRI_LH_CR_DA_LO_0

      [in]   name    registername
      [in]   offset  offset address
      [in]   var     loop variable from *.xls sheet
    """
    def expand_regname(self,name,offset,var):

        if (var == 0):
	    print '{0:35} - {1:10} - {1:10x}'.format(name,offset,hex(offset))
        else:
            for addr in range(0,var):
                b = name.find('$')
                print '{0:35} - {1:10} - {1:10x}'.format((name[0:b]+ str(addr)),(offset+addr),hex(offset+addr))

        print ''


def main():

    workbook = Workbook('workbook1.xls')
    workbook.print_workbook_info()
    workbook.print_registers(True)


if __name__ == '__main__':
    main()
