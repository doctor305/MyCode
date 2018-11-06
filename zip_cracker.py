#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月31日

@author: jinfeng
'''


import zipfile
from threading import Thread
import time
import os


def unzip_by_dic(path,pswd_list,no):
    newpath = path+str(no)
    with open(path,'rb') as f_r:
        with open(newpath,'wb') as f_w:
            f_w.write(f_r.read()) 
    zfile = zipfile.ZipFile(newpath)
    print(u"No.%d号线程已开始运行，对%d个常用密码进行测试 !" % (no,len(pswd_list)))
    for pswd in pswd_list:
        try:
            zfile.extractall(pwd=pswd.encode('utf8'))
            print(u"No.%d号线程运行结束 !\n 加密zip文件--%s 的密码为 ：  %s" % (no,path,pswd))
            zfile.close()
            os.remove(newpath)
            break
        except:
            continue
    else:
        zfile.close()
        os.remove(newpath)
        
    
def get_pwlist():
    pwlist = []
    with open('passwddic.txt','r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            pwlist.append(password)
    return pwlist

def main():
    global path
    path = 'test.zip'
    num_thread = 10
    time_start = time.time()
    pwlist = get_pwlist()
    
    step = len(pwlist)//num_thread+1
    for n in range(num_thread):
        t = Thread(target = unzip_by_dic,args = (path,pwlist[step*n:step*n+step],n+1,))
        t.start()
    t.join()
    time_end = time.time()
    time_use = time_end - time_start
    print(u'用时 %d时%d分%d秒' % (time_use//3600,time_use%3600//60,time_use%60))
    

if __name__ == '__main__':
    main()
