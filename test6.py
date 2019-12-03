# coding=utf-8
import xlrd

'''Execl的使用 cell(0,0).value-第一个值'''

wb=xlrd.open_workbook("test_user_data.xlsx")#打开execl
sh=wb.sheet_by_name("TestUserLogin") #按表名定位工作表
print(sh.nrows) #有效数据行数
print(sh.ncols) #有效数据列数
print(sh.cell(0,0).value) #输出第一行第一列的值 ‘case_name’
print(sh.row_values(0)) #输出第一行的所有值（列表格式）

#将数据和标题组成字典，使数据更清晰
print(dict(zip(sh.row_values(0),sh.row_values(1)))) #（第一行：第二行的值）

#遍历excel,打印所有数据
for i in  range(sh.nrows):#按行遍历
    print(sh.row_values(i))