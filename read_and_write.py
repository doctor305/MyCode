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
    book = xlwt.Workbook(encoding = 'utf8',style_compression=0)
    sheet = book.add_sheet('查询结果')
    for n in range(len(column_name)):
        sheet.write(0,n,column_name[n])
    for m in range(len(values)):
        for l in range(len(column_name)):
            sheet.write(m+1,l,values[m][l])
    book.save(save_path)
    
def read_xls(path):
    pass

def write_csv(column_name,values,save_path):
    '''将values中的内容写入csv中，其中传输变量column_name格式为列表,values为列表的列表'''
    csv_write = csv.writer(open(save_path,'w', newline=''),dialect='excel')
    if column_name != '':
        csv_write.writerow(column_name)
    for line in values:
        csv_write.writerow(line.strip().split(','))

def read_csv(path):
    pass

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
    values = read_txt(path)
    #write_txt('',values,'outputtxt.csv')
    write_csv('',values,'outputcsv.csv')
    
    