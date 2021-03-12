# coding=utf-8
import xlrd


def readExcek(sheet, row, col):
    data = xlrd.open_workbook('.\login.xlsx')  # 文件名以及路径，如果路径或者文件名有中文给前面加一个r拜师原生字符。
    table = data.sheet_by_name(sheet)  # 通过名称获取
    l_data = table.cell_value(row, col)  # 返回单元格中的数据
    if type(l_data) == float:
        return int(l_data)
    else:
        return l_data
