#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
题目：熟悉时间函数。
'''

if __name__ =='__main__':
	import time
	start = time.time()
	for i in range(10000):
		print i
	end = time.time()
	print 'Different is %6.3f' % (end - start)
