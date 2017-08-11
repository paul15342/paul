import xlrd
import xlwt
from xlutils.copy import copy
import os

class Excel:
    """
    Excel表格封装
    1. 读取Excel的数据
    2. 数据写入到Excel中
    """
    def __init__(self):
        p = os.getcwd()
        self.path = p + '/param.xlsx'
        self.rb =xlrd.open_workbook(self.path)
        self.wb = copy(self.rb)
        self.s = self.wb.get_sheet(0)


    def set_style(self,color):
        """写入数据库的样式"""
        font = xlwt.Font()
        font.name = "Times New Roman"
        font.colour_index = color
        style = xlwt.XFStyle()
        style.font = font
        return  style

    def write_result_success(self,i):
        """对结果进行判断,如果结果为1(成功),写入Excel 红色PASS
           如果结果为0(失败),写入Excel 蓝色Fail  11为银绿色  12为蓝色
        """
        try:
            self.s.write(i+1,5,"PASS",self.set_style(11))
        except:
            print('Excel打开ing，不能操作')

    def write_result_fail(self,i):
        try:
            self.s.write(i+1,5, "Fail", self.set_style(12))
        except:
            print('Excel打开ing，不能操作')

    def save(self):
        self.wb.save('result.xls')

Excel = Excel()