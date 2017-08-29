#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：使用lamda创建匿名函数。
'''
 
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y #True = 1, False = 0
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x
 
if __name__ == '__main__':
    a = 10
    b = 20
    print 'The largar one is %d' % MAXIMUM(a,b)
    print 'The lower one is %d' % MINIMUM(a,b)

