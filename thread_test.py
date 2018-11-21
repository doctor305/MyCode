#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年11月21日

@author: jinfeng
'''


from threading import Thread
import time
import random

def play(no):
    print(u"No.%s号线程已开始运行!" % no)
    time.sleep(random.randint(5,10))
    print(u"No.%s号线程运行结束!" % no)

for n in range(10):
    t1 = Thread(target = play,args = (str(n+1),))
    t1.start()
t1.join()

print(u"t1运行结束!!!" )
for m in range(10):
    no = str(m+1)+'+'
    t2 = Thread(target = play,args = (no,))
    t2.start()
t2.join()