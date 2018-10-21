#!/usr/bin/evn python
#-*- coding:utf-8 -*-
'''
Created on 2018年10月19日

@author: jinfeng
'''


from PIL import ImageGrab

def get_screenshot(path):
    im = ImageGrab.grab()
    im.save(path,'jpeg')
    

if __name__ == '__main__':
    get_screenshot("screenshot.jpg")