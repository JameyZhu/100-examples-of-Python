#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：按相反的顺序输出列表的值。
'''

a = ['one', 'two', 'three','four','five']
for i in a[::-1]: #让列表值反过来
    print i

print '=='*10
l = len(a)
for i in range(l):
    n = l-1 - i
    print a[n]
