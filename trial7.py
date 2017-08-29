#!/usr/bin/env python
# coding: UTF-8

'''
将一个列表的数据复制到另一个列表中。
'''

a = [1,2,3]
b = a[:]
print b       # 将a的数据赋值给b 当a的数值发生改变时b不变
a = [1,2,3]
b = a
print b       # 将a的地址赋值给b 当a的数值发生改变时b随之改变
a[0] = 0
print a        # 将a的数据赋值给b 当a的数值发生改变时b不变
print b
a = [1,2,3]
b = a
print b
a[0] = 0
print a         # 将a的地址赋值给b 当a的数值发生改变时b随之改变
print b
