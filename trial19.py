#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''
 
from sys import stdout
for j in range(2,1001):
    k = []
    n = -1
    s = j
    for i in range(1,j):
            if j % i == 0:
                n += 1
                s -= i
                k.append(i)
#    if s == 0: #当这个数和它的因子之和相等时，打印出这个数
#        print j
#        for i in range(n):
#            stdout.write(str(k[i])) #sys.stdout是标准输出文件，write是往这个文件里写数据。总的来说就是打印数据到标准输出。
#            stdout.write(' ') #数据之间留有空格
#        print k[n]
    if s == 0: #当这个数和它的因子之和相等时，打印出这个数
        print j
        print k
