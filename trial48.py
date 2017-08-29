#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：比较数字大小。
'''

if __name__ == '__main__':
    print '第一种方法'
    i = 10
    j = 20
    if i > j:
        print '%d 大于 %d' % (i,j)
    elif i == j:
        print '%d 等于 %d' % (i,j)
    elif i < j:
        print '%d 小于 %d' % (i,j)
    else:
        print '未知'

    print '第二种方法'
    def compare(num1, num2):
        if num1 > num2:
            print("%s大于%s" % (num1, num2))
        elif num2 > num1:
            print("%s大于%s" % (num2, num1))
        else:
            print("%s等于%s" % (num1, num2))

    numOne = input("请输入第一个数字:")
    numTwo = input("请输入第二个数字:")
    compare(numOne, numTwo)
