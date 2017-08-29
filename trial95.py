#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
题目：字符串日期转换成易读的日期格式。
'''

from dateutil import parser
dt1 = parser.parse("Aug 28 2015 12:00AM")
dt2 = parser.parse("July 30 2017 2:00PM")
print dt1
print dt2
