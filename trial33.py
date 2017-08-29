#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

'''
题目：按逗号分隔列表。
'''

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print(s1)

print('第二种方法')
L = repr(L)[1:-1]
print(L)

print('第三种方法')
l = [1,2,3,4,5,6,7]
k = 1
for i in l:
    print(i,end= ('' if (k == len(l)) else ','))
    k +=1
