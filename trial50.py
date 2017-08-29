#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：输出一个随机数。
'''
 
import random
 
#生成 10 到 20 之间的随机数
print random.random() #生成0-1之间的随机数
print random.uniform(10, 20) #生成随机数
print random.randint(10, 20) #生成随机整数

