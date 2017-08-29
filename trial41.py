#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：模仿静态变量的方法。
'''

#静态变量：在静态存储区内分配存储单元。在程序整个运行期间都不释放。
#动态变量：属于动态存储类别，存储在动态存储区空间(而不是静态存储区空间)，函数调用结束后即释放。 

def varfunc():
    var = 0
    print 'var = %d' % var
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()


# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print self.StaticVar

print Static.StaticVar
a = Static()
for i in range(3):
    a.varfunc()

