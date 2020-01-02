import xlrd
import numpy as np
import openpyxl
import sys, getopt

def write(idx,xlsx_path,value):

    wb = openpyxl.load_workbook(xlsx_path)
    ws = wb.active
    ws.cell(row=idx, column=1).value = value
    wb.save(xlsx_path)
    wb.close()

    return 0