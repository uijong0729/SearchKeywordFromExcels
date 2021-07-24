import xlrd as xls
import openpyxl as xlsx
from openpyxl import load_workbook


# 실행키 Ctrl + F5 (VSCode기준)


# xls
# https://xlrd.readthedocs.io/en/latest/
book = xls.open_workbook("myfile.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
#print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
for rx in range(sh.nrows):
    print(sh.row(rx))

print("#########################################")

# xlsx
# https://openpyxl.readthedocs.io/en/stable/
wb = load_workbook(filename = 'myfile2.xlsx')
#sheet_ranges = wb['range names']
#print(sheet_ranges['D18'].value)