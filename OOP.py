#! /usr/bin/env python
# -*- coding: utf-8 -*-

import types
import hello

class Student(object):
	def __init__(self):
		pass

	def __getattr__(self, attr):
		if attr=='score':
			return 99

	def print_score(self):
		print 'name is %s, score is %s' % (self.name , self.score)

# lisa = Student('Lisa Tam',99)
# lisa.print_score()


class Person(object):
	def __init__(self,name):
		self.__name = name

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def __str__(self):
		return 'Person name is %s' % self.__name

person = Person('kangkang')
# person.name = 'kangkang'
person.set_name('xixi')
# print person._Person__name

class Animal(object):
	def run(self):
		print 'Animal is running'

class Dog(Animal):
	def run(self):
		print 'Dog is running'

class Cat(Animal):
	def run(self):
		print 'Cat is running'

def run_twice(animal):
	animal.run()

# run_twice(Animal())
# run_twice(Dog())
# print type(abs)

# print type('abc') == types.StringType
# print type(u'abc') == types.UnicodeType
# print type(123) == types.IntType
# print type([]) == types.ListType
# print type({}) == types.DictionaryType
# print dir('abc')
# print hasattr(lisa,'name')
# print hasattr(person,'set_name')
# print hasattr(person, 'haha')

s = Student()

def set_age(self,age):
		self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
# print s.age

Student.set_age = MethodType(set_age, None, Student)

aa = Student()
aa.set_age(10);
# print aa.age

class Car(object):
	@property
	def price(self):
		return self._price
	@price.setter
	def price(self, value):
		if not isinstance(value, int):
			raise ValueError('price must be an integer')
		if value < 0:
			raise ValueError('price must be greater than 0')
		self._price = value

	def get_price(self):
		return self._price

	def set_price(self, value):
		if not isinstance(value, int):
			raise ValueError('price must be an integer')
		if value < 0:
			raise ValueError('price must be greater than 0')
		self._price = value

c = Car()
c.name = 'BMW'
# c.score = 99
# print c.score
# lamborghini = Car()
# lamborghini.set_price(1000000)
# print lamborghini.get_price()
c.price = 10000
# print c.price
# c.price = -1
# print c.price

ss = Person('kangkang')
# print ss

class Fib(object):
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self

	def __getitem__(self,n):
		if isinstance(n, int):
			a,b = 1,1
			for x in range(n):
				a,b = b, a+b
			return a

		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a,b=1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

	def next(self):
		self.a,self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration();
		return self.a

# for n in Fib():
# 	print n
# f = Fib()
# print f[2]
# print range(100)[5:10]
# f = Fib()
# print f[0:5]
# ss = Student()
# print ss.score

class Chain(object):
	def __init__(self,path=''):
		self._path = path

	def __getattr__(self,path):
		return Chain('%s/%s' % (self._path,path))

	def __str__(self):
		return self._path

	def __call__(self):
		print 'this is a chain'


# print Chain().status.user.timeline.list
c = Chain()
# print c()

# print callable(c)
# print callable([1,2,3])
# print callable(max)
# print callable(None)

from hello import Hello
# h = Hello()
# print h.hello()
# print (type(Hello))
# print (type(h))

def fn(self, name='world'):
	print('Hello,%s' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()
# print type(h)
# print type(Hello)

class ListMetaClass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value:self.append(value)
		return type.__new__(cls,name,bases,attrs)

class MyList(list):
	__metaclass__ = ListMetaClass

L = MyList()
L.add(1)
print L



















