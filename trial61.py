#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：打印出杨辉三角形（要求打印出10行如下图）。
'''
 
if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print

    print
    n = int(raw_input('请输入杨辉三角形的层级：\n'))
    def lst(i,j):
        if i == j or j ==1:
            return 1
        else:
            return lst(i-1,j-1) + lst(i-1,j) #上一层左侧数据和上一层对应数据之和
    for i in range(1, n+1):#i是指第几层
        for j in range(1,i + 1):#j是某一层的第几个数
           # print lst(i,j)
            stdout.write(str(lst(i,j)))
            stdout.write(' ')
        print
