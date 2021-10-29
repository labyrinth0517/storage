import xlrd
from tool1 import *

wb = xlrd.open_workbook(filename='excelD7.xls')

for i in range(12):
    ts = wb.sheet_by_index(i)
    for j in range(1, ts.nrows):
        gcv = ts.row_values(j)
        sql1 = 'insert into saleDat value(%s,%s,%s,%s,%s)'
        param1 = [gcv[0], gcv[1], gcv[2], gcv[3], gcv[4]]
        update(sql1, param1)

print('end.')
