#!/usr/bin/env python
# coding: UTF-8

if __name__ == '__main__':
	for i in range(7):
		a = int(raw_input('Input a number:\n'))
		while a<1 or a > 50:
			a = int(raw_input('Input a number:\n'))
		print a * '*'
