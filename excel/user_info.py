import xlrd
from excel.apiClient import get

workbook = xlrd.open_workbook('user_info.xlsx')
worksheet = workbook.sheet_by_name('db')
list = worksheet._cell_values

for row in list[1:]:
    print(get(row[0], row[1], row[2]))
