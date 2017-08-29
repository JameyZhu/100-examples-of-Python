#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：统计1到100之和。
'''
 
tmp = 0
for i in range(1,101):
    tmp += i
print 'The sum is %d' % tmp

print
print 'The sum is', sum(range(1,101))

