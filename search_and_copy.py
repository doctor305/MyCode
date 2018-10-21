#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月19日

@author: jinfeng
'''


import os
import re
import os.path

def search_file(path,extension):
    '''遍历路径path下所有目录和文件，返回后缀符合extension文件的列表'''
    list_files = []
    for root,dirs,files in os.walk(path):   #遍历指定路径path下所有目录和文件
        for name in files:
            if name[-len(extension):]==extension:
                list_files.append(root+os.sep+name)  #将后缀符合extension变量的文件添加至list_files
    return list_files

def copy_file(s_file,t_file):
    '''将文件s_file的内容复制到文件t_file'''
    with open(s_file,'r') as f_r:
        with open(t_file,'w') as f_w:
            f_w.write(f_r.read())

def search_file_by_key(path,key):
    '''遍历目录path下所有文件，按照文件名筛选出符合条件key的文件加入列表作为返回。key为正则表达式字符串'''
    list_files = []
    for root,dirs,files in os.walk(path):   #遍历指定路径path下所有目录和文件
        for name in files:
            file_path = root+os.sep+name
            if os.path.isfile(file_path) and re.search(key,name):
                list_files.append(file_path)  #将符合条件的文件添加至list_files
    return list_files

def search_filecontent_by_key(path,key):
    '''遍历目录path下所有文件，按照文件内容筛选出符合条件key的文件加入列表作为返回。'''
    list_files = []
    for root,dirs,files in os.walk(path):   #遍历指定路径path下所有目录和文件
        for name in files:
            file_path = root+os.sep+name
            if os.path.isfile(file_path):
                try:
                    with open(file_path,'r') as f:
                        content = f.read()
                        if re.search(key,content):
                            list_files.append(file_path)  #将符合条件的文件添加至list_files
                except:
                    pass
    return list_files
            
            
if __name__ == "__main__":
#     filelist = search_file('sdir','.txt')
#     print(filelist)
#     for file in filelist:
#         copy_file(file,'tdir'+os.sep+file.split(os.sep)[-1])
#         with open(file,'r') as f:
#             print(f.read())
#    ls = search_file_by_key('.',r'^test')
    ls = search_filecontent_by_key('.',r'abcd')
    print(ls)