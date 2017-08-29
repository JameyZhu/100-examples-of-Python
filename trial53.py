#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位异或 ^ 。
'''

# ^ 按位异运算：当两对应的二进位相异时，该位结果为1。
if __name__ == '__main__':
    a = 077
    b = a ^ 3
    print 'The a ^ 3 = %d' % b
    b ^= 7
    print 'The a ^ b = %d' % b
