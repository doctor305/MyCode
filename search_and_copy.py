#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月19日

@author: jinfeng
'''


import os

def search_file(path,extension):
    list_files = []
    for root,dirs,files in os.walk(path):
        for name in files:
            if name[-len(extension):]==extension:
                list_files.append(root+os.sep+name)
    return list_files

def copy_file(s_file,t_file):
    with open(s_file,'r') as f_r:
        with open(t_file,'w') as f_w:
            f_w.write(f_r.read())

            
            
if __name__ == "__main__":
    filelist = search_file('sdir','.txt')
    print(filelist)
    for file in filelist:
        copy_file(file,'tdir'+os.sep+file.split(os.sep)[-1])
        with open(file,'r') as f:
            print(f.read())