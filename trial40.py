#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：将一个数组逆序输出。
'''
 
if __name__ == '__main__':
    #第一种方法
    a = [9,6,5,4,1]
    N = len(a) 
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print a

    #第二种方法
    b = [9,6,5,4,1]
    print b
    b.reverse()
    print b
