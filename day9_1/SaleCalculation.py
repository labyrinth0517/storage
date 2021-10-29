import xlrd
from tool1 import *

wb = xlrd.open_workbook(filename='excelD7.xls')
param1 = []

for i in range(1):
    ts = wb.sheet_by_index(i)
    for j in range(1, 10):
        gcv = ts.row_values(j)
        for x in gcv:
            param1.append(x)
        sql1 = 'insert into saleDat value(%s,%s,%s,%s,%s)'
        update(sql1, param1)
        param1 = []
print('end.')
