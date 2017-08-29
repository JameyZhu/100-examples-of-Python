#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：熟悉时间函数。
'''

if __name__ == '__main__':
    import time
    print time.ctime(time.time())
    print time.asctime(time.localtime(time.time()))
    print time.asctime(time.gmtime(time.time()))
