#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n + 1,2):
        s += 1.0 / i   # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def podd(n):
    s = 0.0
    for i in range(1, n + 1,2):
        s += 1.0 / i    # Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
    return s
 
def dcall(fp,n):
    s = fp(n)
    return s
 
if __name__ == '__main__':
    n = int(raw_input('input a number:\n'))
    if n % 2 == 0:
        sum1 = dcall(peven,n)
    else:
        sum1 = dcall(podd,n)
    print sum1


    print '==' * 10
    def sumfr(n):
        ls = [1.0/i for i in range(n,0,-2)]
        return sum(ls)

    print sumfr(n)

