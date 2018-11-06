#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月31日

@author: jinfeng
'''


import zipfile
from threading import Thread
import time


def unzip(zipfile,password):
    try:
        zfile.extractall(pwd=password.encode('utf8'))
    except:
        return False
    return password

def unzip_by_dic(zipfile,pswd_list):
    global tag
    for pswd in pswd_list:
        if tag == True:
            break
        try:
            zfile.extractall(pwd=password.encode('utf8'))
        except:
            continue
        print(pswd)
        tag = True
        break
    
def get_pwlist():
    pwlist = []
    with open('passwddic.txt','r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            pwlist.append(password)
    return pwlist

def main():
    global tag
    path = 'test2.zip'
    num_thread = 10
    tag = False
    pwlist = get_pwlist()
    zfile = zipfile.ZipFile(path)
    step = len(pwlist)//num_thread+1
    for n in range(num_thread):
        t = Thread(target = unzip_by_dic,args = (zfile,pwlist[step*n:step*n+step]))
        

if __name__ == '__main__':
    main()
