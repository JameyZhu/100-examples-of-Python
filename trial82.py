#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：八进制转换为十进制
'''
 
if __name__ == '__main__':
    n = 0
    p = raw_input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print n

    def f8to10(num):
        print("8进制数：", num)
        l = str(num)
        length = len(l)
        sum = 0
        for i in range(length):
            sum += 8 ** i * int(l[length-1-i])
        print("转成10进制数为：",sum)

    f8to10(122)
