#!/usr/bin/env python
#coding: UTF-8

'''
题目：将列表转化为字典。
'''

i = ['a','b']
l = [1,2]

print dict([i,l])

l1 = [1,2,3,4,5,6]
l2 = ['aa','bb','cc','dd','ee','ff']
d={}
for index in range(len(l1)):
    d[l1[index]]=l2[index] # 注意，key 若重复，则新值覆盖旧值 
print d

l1=[1,2,3,6,87,3]
l2=['aa','bb','cc','dd','ee','ff']
d1={}
for index in range(len(l1)):
    d1[l1[index]]=l2[index] # 注意，key 若重复，则新值覆盖旧值 
print d1
