#! /usr/bin/python
# -*- coding: UTF-8 -*-
# Filename : helloworld.py

import math
import sys   
sys.setrecursionlimit(1000000)
from collections import Iterable
import os
import functools
import hello

if 0:
	######################################################
	print 'Hello World'
	print 'This is','my first python','program'

	name = raw_input('please input your name:')
	print 'Hello',name

	a = 100
	if a>=0:
		print a
	else:
		print -a

	print 'I\'m \"OK\"'

	print '''line1
	...line2
	...line3
	'''
	print 5>3 and 5>2
	######################################################
	a = 100
	a = 'ABC'
	print a

	print ord('A')
	print chr(65)
	print len(u'ABC')
	print len(u'中文')
	print len('\xe4\xb8\xad\xe6\x96\x87')
	print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
	print 'Hello, %s' % 'world'
	print 'I am %s, %s years old' % ('kangkang',26)
	print u'我的名字是 %s' % u'谭智康'

	######################################################
	language = ['objective-c','java','python']
	language.append('c++')
	language.insert(1,'swift')
	print language.pop()
	print language[0]
	print language[1]
	print language[2]
	print language[3]

	language = ['objective-c','c#','javascript']
	person = ['kangkang',26,language]
	print person[2][1]

	t = (1,'kangkang')
	print t

	######################################################
	language = ['objective-c','java','python']
	for lan in language:
		print lan

	scores = {'chinese':98,'maths':95,'english':92}
	scores['policy'] = 90
	print scores.get('policy')
	print 'maths' in scores
	print scores['maths']	

	######################################################
	s1 = set([1,2,3,1,1,2])
	s2 = set([3,4,5,6])
	print s1 & s2
	print s1 | s2

	sor = ['b','a','c']
	sor.sort()
	print sor

	t = (1,2,4)
	d = {t:'tuple'}
	print d

	s = set([t,123])
	print s
	######################################################
	print abs(-20)
	print int('123')

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x

def nope():
	pass

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

# x,y = move(100,100,60,math.pi/6)
# print x,y

def power(x,n=2):
	s = 1
	while n>0:
		n = n - 1
		s = s * x
	return s

# print power(3,3)
# print power(5)

def add_end(L=[]):
	
	L.append('END')
	return L

# l = add_end()
# print id(l)
# a = add_end() 
# print id(a)

def calc(numbers):
	sum = 0
	for num in numbers:
		sum = sum + num * num
	return sum

nums = [1,2,3]
# print calc(nums)

def calParam(*numbers):
	sum = 0
	for num in numbers:
		sum = sum + num * num
	return sum

# print calParam(*nums)

def person(name, age, **kw):
	print 'name:',name,'age:',age,'other:',kw

kw = {'city':'beijing','gender':'M'}
# person('kangkang',30,**kw)

def func(a,b,c=0,*args,**kw):
	print 'a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw

args = (1,2,3,4)
kw = {'x':99}
# func(*args,**kw)

def kk(a,b,*c):
	print 'a=',a,'b=',b,'c=',c

# L = [1,2,4,5]
# kk(1,2,*L)

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

# print fact(1000)

def highProperty(n):
	L = []
	while n > 0:
		L.append(n)
		n = n - 2
	return L

# print highProperty(99)

L = range(100)
# print L[0:10]
# print L[-10:]
# print L[10:20]
# print L[0:10:2]
# print (1,2,3,4,5)[0:3]
# print 'ABCDEFG'[0:3]

# d = {'a':1,'b':2,'c':3}
# for key,value in d.iteritems():
# 	print key,value

# for ch in 'ABC':
# 	print ch

# print isinstance('abc',Iterable)
# print isinstance([1,2,4],Iterable)
# print isinstance(set({1,2,3}),Iterable)

# for i,value in enumerate(['a','b','c']):
# 	print i,value

# print range(0, 10)

# L = []
# for n in range(1, 11):
# 	L.append(n * n)
# print L

# print [x * x for x in range(1,11) if x % 2 == 0]

# print [m + n for m in 'ABC' for n in 'XYZ']

# print [d for d in os.listdir('.')]

# d = {'x':'A','y':'B','z':'C'}
# print [k + '=' + v for k,v in d.iteritems()]

# L = ['HELLO','WORLD','SWIFT','IOS']
# print [k.lower() for k in L]

# x='abc'
# y=123
# print isinstance(x,str)
# print isinstance(y,number)

L = ['a','b','c',18, None]
# print [k for k in L if isinstance(k, str)]

# L = [x*x for x in range(10)]
# print L
# g = (x *x for x in range(10))
# for n in g:
# 	print n

def fib(maxValue):
	n,a,b = 0,0,1
	while n < maxValue:
		yield b
		a,b = b, a+b
		n = n+1

# fib = fib(6)
# print fib.next()

# print fib(6)
# for n in fib(6):
# 	print n
# l = [x for x in fib(10)]
# print l[1:3]
# def fibSlice(start, end):
# 	print [x for i,x in enumerate(fib(end)) if i >= start]

# fibSlice(0,6)

def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

o = odd()
# print o.next()
# print o.next()
# print o.next()
# print o.next()

# f = abs
# print f(-10)

def add(x,y,f):
	return f(x) + f(y)

def judge(x):
	if x >= 10:
		return 10
	return x

# print add(10,5,judge)

def f(x):
	return x * x
# print map(f,[1,2,3,4,5])

# reduce(f,[x1,x2,x3,x4]) = f(f(f(x1, x2), x3), x4)
def add(x,y):
	return x + y

# print reduce(add, [1,2,3,4,5])
# print sum([1,2,3,4,5,6])
def fn(x, y):
	return x * 10 + y
# print reduce(fn, [1,3,5,7,9])

def str2int(s):
	def fn(x,y):
		return x * 10 + y
	def char2sum(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2sum, s))

# print str2int('13579')

def convertToUpperCase(name):
	result = ''
	for k,v in enumerate(name):
		if k == 0:
			result += v.upper()
		else:
			result += v.lower()
	return result

def normalisze(name):
	return name[0].upper() + name[1:].lower()

# print normalisze('kangkang')
# print map(normalisze, ['adam', 'LISA', 'barT'])

def is_odd(n):
	return n % 2 == 0
# print filter(is_odd, [1,2,3,4,5,6,7,8,9])

def not_empty(n):
	return n and n.strip()
# print filter(not_empty, ['1','','2','  ',None, '3'])

# print sorted([36,4,1,3,10])

def reverse_cmp(x,y):
	if x > y:
		return -1
	elif x < y:
		return 1
	else:
		return 0

# print sorted([36,4,1,3,10], reverse_cmp)

def cmp_ignore_case(x,y):
	a = x.upper()
	b = y.upper()
	if a < b:
		return -1
	elif a > b:
		return 1
	else:
		return 0

# print sorted(['a','C','B','D'],cmp_ignore_case)

def calc_sum(*args):
	sum = 0
	for x in args:
		sum = sum + x
	return sum

args = [1,2,3]
# print calc_sum(*args)

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,3,5,7,9)
# print f()

def count():
	fs = []
	for x in range(1,4):
		def f():
			return x * x
		fs.append(f)
	return fs

f1,f2,f3 = count()
# print f1()
# print f2()
# print f3()
# print map(lambda x:x*x , [1,2,3,4,5,6])

def log (func):
	def wrapper(*args, **kw):
		print 'call %s():',func.__name__
		return func(*args, **kw)
	return wrapper

@log
def build():
	return lambda x,y,z:x*x+y*y+z*z

# print build()
# print build()(1,2,3)

def log2(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print 'call %s():' % func.__name__
		return func(*args, **kw)
	return wrapper

def now2():
	print 'haha'
now2 = log2(now2)
# now2()

def printLog(func):
	@functools.wraps(func)
	def decorator(*args,**kw):
		print 'call begin'
		return func(*args, **kw)
	return decorator

def testFunc():
	print 'I am test function'

printFunc = printLog(testFunc)
# printFunc()


import functools
def log3(args):
    text = "just call"
    def decoration(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text,func.__name__)
            result = func(*args, **kw)
            return result
        return wrapper
    if hasattr(args, '__call__'):
        #返回decoration内层函数wrapper
        return decoration(args)
    else:
        text = args
        #直接返回decoration
        return decoration

@log3
def f1():
    pass

@log3("excute")
def f2():
    pass

# f1()
# f2()

# print int('11',base=2)
def int2(x,base=2):
	return int(x,base)
# print int2('10',2)

intFor2 = functools.partial(int, base=2)
# print intFor2('10')

max2 = functools.partial(max,10)
args = (2,5,6)
# print max2(*args)

print hello.test()
















