#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：文本颜色设置。
'''
#关于文本的颜色设置还需要进一步的学习

class bcolors:
    HEADER = '\033[95m' #紫色
    OKBLUE = '\033[94m' #蓝色
    OKGREEN = '\033[92m' #绿色
    WARNING = '\033[93m' #黄色
    FAIL = '\033[91m' #深红色
    ENDC = '\033[0m' #关闭所有属性
    BOLD = '\033[1m' #设置高亮度
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC
print bcolors.OKGREEN + "警告的颜色字体?" + bcolors.ENDC
print bcolors.OKBLUE + "警告的颜色字体?" + bcolors.FAIL
