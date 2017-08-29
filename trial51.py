#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：学习使用按位与&。
'''

# & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
# | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
# ^ 按位异或运算符：当两对应的二进位相异时，结果为1 。
# ~ 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
# << 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
# >> 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数。 


if __name__ == '__main__':
    a = 077
    b = a & 3
    print 'a & b = %d' % b
    b &= 7
    print 'a & b = %d' % b

    a = 60            # 60 = 0011 1100
    b = 13            # 13 = 0000 1101
    print 'a=',a,':',bin(a),'b=',b,':',bin(b) #bin函数将输入的十进制转换成二进制。
    c = 0
    c = a & b;        # 12 = 0000 1100
    print "result of AND is ", c,':',bin(c)
    c = a | b;        # 61 = 0011 1101 
    print "result of OR is ", c,':',bin(c)
    c = a ^ b;        # 49 = 0011 0001
    print "result of EXOR is ", c,':',bin(c)
    c = ~a;           # -61 = 1100 0011
    print "result of COMPLEMENT is ", c,':',bin(c)
    c = a << 2;       # 240 = 1111 0000
    print "result of LEFT SHIFT is ", c,':',bin(c)
    c = a >> 2;       # 15 = 0000 1111
    print "result of RIGHT SHIFT is ", c,':',bin(c)
