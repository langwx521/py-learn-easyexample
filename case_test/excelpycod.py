import xlrd

data = xlrd.open_workbook('../practice/instance.xls')

tables = data.sheets()[0]

print (tables)
# print (tables.nrows)
# print (tables.cell_value(1,4))
# print (tables.cell_value(2,1))
