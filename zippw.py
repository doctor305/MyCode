#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月31日

@author: jinfeng
'''


import zipfile



def unzip(path,password):
    zfile = zipfile.ZipFile(path)
    try:
        zfile.extractall(pwd=password.encode('utf8'))
    except:
        return False
    return password

def unzip_by_dic(path):
    with open('passwddic.txt','r') as f:
        for line in f.readlines():
            password = unzip(path,line.strip('\n'))
            if password != False:
                print(password)
                break

if __name__ == '__main__':
    unzip_by_dic('test.zip')
