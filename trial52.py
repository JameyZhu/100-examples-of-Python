#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位或 | 。
'''

#按位运算符是把数字看作二进制来进行计算的。
#'|'按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。

if __name__ == '__main__':
    a = 077
    b = a | 3
    print 'a | b is %d' % b
    b |= 7
    print 'a | b is %d' % b
