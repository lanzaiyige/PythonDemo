#! /usr/bin/env python
# -*- coding: utf-8 -*-

'a test module'
__author__ = 'tanzhikang'
import sys
from PIL import Image

try:
	import cStringIO as StringIO
except ImportError:
	import StringIO

try:
	import json
except ImportError:
	import simplejson as json

class Hello(object):
	def hello(self, name='world'):
		print('Hello ,%s' % name)

def test():
	args = sys.argv
	if(len(args)) == 1:
		print 'Hello World!'
	elif len(args) == 2:
		print 'Hello %s' % args[1]
	else:
		print 'Too many arguments'

def _test():
	print sys.path
	
# if __name__ == '__main__':
# testImage = Image.open("test.jpg")
# testImage.show()

class Animal(object):
	pass

class Runnable(object):
	def run():
		print 'Runnnig..'

class Dog(Animal,Runnable):
	pass

class Bat(Animal):
	pass

class Parrot(Animal):
	pass

class Ostrich(Animal):
	pass

g = lambda x:x+1
# print g(1)

foo = [1,2,3]
# print [x * 2 for x in foo]