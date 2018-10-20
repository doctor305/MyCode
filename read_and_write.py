#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018��10��19��

@author: jinfeng
'''

import xlrd
import xlwt
import csv
import os

def write_xls(column_name,values,save_path): 
    sheet_name = '查询结果'
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
    '''excel电子表单工作表读取，将工作表内容通过列表形式返回'''
    pass
    
def read_xls_allsheets(path,tag_columnname):
    '''excel电子表多工作表读取，将多个工作表内容合并在一起通过列表形式返回,多个工作表格式必须相同'''
    pass

def write_csv(column_name,values,save_path):
    '''将values中的内容写入csv中，其中传输变量column_name格式为列表,values为列表的列表'''
    csv_write = csv.writer(open(save_path,'w', newline=''),dialect='excel')
    if column_name != '':
        csv_write.writerow(column_name)
    for line in values:
#        csv_write.writerow(line.strip('\n').split(','))
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

if __name__ == "__main__":
    path = 'sdir'+os.sep+'test01.txt'
#     for i in range(100):
#         with open(path,'a') as f:
#             f.write(str(i)+','+'A'+str(i)+','+str(i*5)+'\t\n')
    #write_xls()
    #read_xls()
    #write_csv()
    #read_csv()
    #write_txt()
    #values = read_txt(path)
    #write_txt('',values,'outputtxt.csv')
    #write_csv('',values,'outputcsv.csv')
    values = read_csv('outputcsv.csv')
    write_xls('',values,'xls01.xls')
    
    