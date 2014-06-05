import sys
import xlrd


class Workbook:

    def __init__(self):

        self.workbook = xlrd.open_workbook('workbook1.xls')

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

        print 'Register                                    loop   offset address'

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
         	    print reg_name,
		    print addr_offset


    """
      expand register name according to loop variable found in the *.xls sheet
      CRI_LH_CR_DA_LO_$k => CRI_LH_CR_DA_LO_0

      [in]   name    registername
      [in]   offset  offset address
      [in]   var     loop variable from *.xls sheet
    """
    def expand_regname(self,name,offset,var):

        if (var == 0):
            print name,
            print '\t',offset
        else:
            for addr in range(0,var):
                b = name.find('$')
                print name[0:b]+ str(addr),
                print '\t',offset+addr

        print ''


def main():

    workbook = Workbook()
    workbook.print_workbook_info()
#    workbook.print_registers()
    workbook.print_registers(True)


if __name__ == '__main__':
    main()
