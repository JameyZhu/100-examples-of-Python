#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：用*号打印出菱形
'''
 
from sys import stdout
for i in range(6):
    for j in range(6 - i + 1):
        stdout.write(' ') #空格
    for k in range(6 * i + 1):
        stdout.write('*')
    print
 
for i in range(5):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(6 - 4 * i + 1):
        stdout.write('*')
    print

