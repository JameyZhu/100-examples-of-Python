#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''
 
Tn = 0
Sn = []
n = int(raw_input('n = '))#相加数字的个数
a = int(raw_input('a = ')) #重复的数字
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn
 
Sn = reduce(lambda x,y : x + y,Sn)#内置reduce函数，将函数作用于每一个列表，此处就是sn列表求和
print "计算和为：",Sn

