#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：利用递归方法求5!。
'''
 
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum

n = int(raw_input('请输入一个整数：\n')) 
for i in range(n+1):
    print '%d! = %d' % (i,fact(i))

