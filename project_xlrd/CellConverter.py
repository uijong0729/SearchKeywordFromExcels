import openpyxl as xlsx
import xlrd as xls
from openpyxl import Workbook

class XlsxCellConverter:   
    def read_all(self, workbook):
        worksheet = workbook.active
        for row in worksheet.iter_rows():
            for cell in row:
                if cell.value != None:
                    print("[xlsx cell Converter] ", cell.value)

class XlsCellConverter:
    def read_all(self, workbook):
        sheet_names = workbook.sheet_names()
        for sheet_name in sheet_names:
            sheet = workbook.sheet_by_name(sheet_name)
            num_cols = sheet.ncols
            for row_idx in range(0, sheet.nrows):
                print ('Row: %s' % row_idx)
                for col_idx in range(0, num_cols):
                    cell_obj = sheet.cell(row_idx, col_idx)
                    print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj)) 