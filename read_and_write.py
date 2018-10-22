#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月19日

@author: jinfeng
'''

import xlrd
import xlwt
import csv
import os
import xlsxwriter

def write_xls(column_name,values,save_path): 
    sheet_name = u'输出表'
    book = xlwt.Workbook(encoding = 'utf8',style_compression=0)
    sheet = book.add_sheet(sheet_name)
    tag = 0
    if column_name != '':    #当输入的column_name不为空时，空出一行插入表头，置tag值为1，随后插入内容时的行号在原有值基础上增1
        for n in range(len(column_name)):
            sheet.write(0,n,column_name[n])
        tag = 1
    for m in range(len(values)):
        for l in range(len(values[0])):
            sheet.write(m+tag,l,values[m][l])
    book.save(save_path)

def read_xls(path):
    '''excel电子表单个工作表读取，将工作表内容通过列表形式返回，只读取电子表中的第一个sheet'''
    workbook = xlrd.open_workbook(path)
    output = []
    table = workbook.sheet_by_index(0)
    for i in range(table.nrows):
        output.append(table.row_values(i))
    return output
    
def read_xls_allsheets(path,tag_columnname):
    '''excel电子表多工作表读取，将多个工作表内容合并在一起通过列表形式返回,多个工作表格式必须相同
    tag_columnname表示是否含有表头，工作表不含表头,tag_columnname为False，含有表头,tag_columnname为True，读取数据时跳过第一行'''
    workbook = xlrd.open_workbook(path)
    output = []
    columnname = []
    for i in range(len(workbook.sheet_names())):
        table = workbook.sheet_by_index(i)
        if table.nrows>0:
            for j in range(table.nrows):
                if tag_columnname and j == 0:
                    if len(columnname)==0:
                        columnname.append(table.row_values(j))  #将表头插入列表columnname中，以便在最终的返回列表output中插入表头
                    continue  #含有表头的工作表读取数据时跳过第一行
                output.append(table.row_values(j))
    if tag_columnname:
        return columnname+output
    else:
        return output
    

def write_csv(column_name,values,save_path):
    '''将values中的内容写入csv中，其中传输变量column_name格式为列表,values为列表的列表'''
    csv_write = csv.writer(open(save_path,'w', newline=''),dialect='excel')
    if column_name != '':
        csv_write.writerow(column_name)
    for line in values:
###        csv_write.writerow(line.strip('\n').split(','))
        csv_write.writerow(line)

def read_csv(path):
    '''读取path的csv格式文件，将读取到的内容以元素为列表的列表格式返回，如 [[1,'a'],[2,'b'],[3,'c']]'''
    csv_reader = csv.reader(open(path,'r'))
    output = []
    for line in csv_reader:
        output.append(line)
    return output

def write_txt(column_name,values,save_path):
    f = open(save_path,'w')
    if column_name != '':
        f.write(column_name+'\t\n')
    for i in values:
        f.write(i+'\t\n')
    f.close()

def read_txt(path):
    output = []
    with open(path,'r') as f:
        for i in f.readlines():
            output.append(i.strip('\t\n'))
    return output

def write_xlsx(column_name,values,save_path):
    workbook = xlsxwriter.Workbook(save_path)
    sheet = workbook.add_worksheet()
    tag = 0
    if column_name != '':    #当输入的column_name不为空时，空出一行插入表头，置tag值为1，随后插入内容时的行号在原有值基础上增1
        for n in range(len(column_name)):
            sheet.write(0,n,column_name[n])
        tag = 1
    for m in range(len(values)):
        for l in range(len(values[0])):
            sheet.write(m+tag,l,values[m][l])
    workbook.close()

def Consolidated():
    '''合并当前目录下所有文本数据，所合并文本数据的格式必须一致'''
    pass

if __name__ == "__main__":
    #path = 'sdir'+os.sep+'test01.txt'
    values = []
    for i in range(100000):
        values.append([str(i),'A'+str(i),str(i*5)])
    print(len(values))
    #write_txt('',values,'outputtxt.csv')
    #write_csv('',values,'outputcsv.csv')
    #values = read_csv('outputcsv.csv')
    write_xlsx('',values,'xls01.xlsx')
    #output = read_xls_allsheets('xls01.xls',False)
    #output = read_xls_allsheets('sdir'+os.sep+'xlsx01.xlsx',False)

    