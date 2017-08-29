#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半再落下。求它在第10次落地时，共经过多少米？第10次反弹多高？
'''
 
tour = []
height = []
 
hei = 100.0 # 起始高度
tim = 10 # 次数
 
for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei) 
    hei /= 2
    height.append(hei)
 
print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))

print '++++' * 10
def tan1(n):
    return 100.0000 / 2 ** n
hei1 = tan1(10)
print('第10次反弹高度：height = {0}'.format(hei1))

n = int(raw_input('请输入弹跳的次数：\n'))

tour1 = [100]
for i in range(1,n+1):
    hei1 = tan1(i)
    tour1.append(hei1)

print tour1 
print('总高度：tour = {0}'.format(sum(tour1)))

print '递归方法'

def fun1(n):
    if n == 0:
        hei2 = 100.00
        return hei2
    return fun1(n-1)/2

hei2 = fun1(10)
print hei2
