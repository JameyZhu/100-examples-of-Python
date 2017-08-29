#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：斐波那契数列。请输入n个斐波那契数。
'''
print '常规方法'
def fib(n):
    l = []
    a,b = 1,1
    l.append(a)
    for i in range(n-1):
        a,b = b,a+b
   # return a
        #print a
        l.append(a)
    return l
# 输出了第10个斐波那契数列
print fib(10)
print fib(15)

print
print '使用递归的方法'
def fib(n):
    if n ==1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

print fib(10)

print

def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print fib(15)
