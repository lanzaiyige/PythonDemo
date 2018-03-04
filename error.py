#! usr/bin/env/python
# -*- coding: utf-8 -*-

import logging

# def foo():
# 	r = some_function()
# 	if r == (-1):
# 		return (-1)
# 	return r

# def bar():
# 	r = foo()
# 	if r == (-1):
# 		print 'Error'
# 	else:
# 		pass

# try:
# 	bar()
# except StandardError, e:
# 	print 'error is ',e

# try:
#     print 'try...'
#     r = 10 / int('2')
#     print 'result:', r
# except ValueError, e:
#     print 'ValueError:', e
# except ZeroDivisionError, e:
#     print 'ZeroDivisionError:', e
# else:
#     print 'no error!'
# finally:
#     print 'finally...'
# print 'END'

# def foo(s):
# 	return 10/s

# def bar(s):
# 	return foo(s)*2

# def main():
# 	bar('0')

# try:
# 	bar('a')
# except StandardError as e:
# 	print 'error is %s' % e
# finally:
# 	print 'END'


# class FooError(StandardError):
# 	pass

# def testFoo(s):
# 	n = int(s)
# 	if n == 0:
# 		raise FooError('invaild value:%s' % s)
# 	return 10/n

# print testFoo('0')

def foo(s):
	n = int(s)
	return 10 / n

def bar(s):
	try:
		foo(s) * 2
	except ZeroDivisionError:
		print 'Error'
		raise ValueError('input error!')

def main():
	bar(0)

main()

logging.basicConfig(level=logging.INFO)












