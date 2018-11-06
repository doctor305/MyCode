#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月31日

@author: jinfeng
'''


import zipfile
from threading import Thread
import time


def unzip_by_dic(zipfile,pswd_list):
    global tag
    print("Start!")
    print(len(pswd_list))
    print(tag)
    for pswd in pswd_list:
        if tag == True:
            print("End!")
            break
        try:
            zipfile.extractall(pwd=pswd.encode('utf8'))
            print('Password is %s' % pswd)
            tag = True
            print("End!")
            break
        except:
            continue
        
    
def get_pwlist():
    pwlist = []
    with open('passwddic.txt','r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            pwlist.append(password)
    return pwlist

def main():
    global tag
    path = 'test.zip'
    num_thread = 5
    tag = False
    time_start = time.time()
    pwlist = get_pwlist()
    print(len(pwlist))
    zfile = zipfile.ZipFile(path)
    step = len(pwlist)//num_thread+1
    for n in range(num_thread):
        t = Thread(target = unzip_by_dic,args = (zfile,pwlist[step*n:step*n+step],))
        t.start()
    t.join()
    print(tag)
    print('End')
    time_end = time.time()
    time_use = time_end - time_start
    print(u'用时 %d时%d分%d秒' % (time_use//3600,time_use%3600//60,time_use%60))
        

if __name__ == '__main__':
    main()
