#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：找到字典年龄最大的人，并输出。
'''
 
if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key
 
    print '%s,%d' % (m,person[m])

    import operator
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    print max(person.iteritems(), key=operator.itemgetter(1))[0]    # 获取最大值的 key
    print max(person.values())                                      # 获取最大值
