#! /usr/bin/python
# -*- coding: UTF-8 -*-


from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
import base64
import hashlib

Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
# print p.x
# print p.y

Circle = namedtuple('Circle', ['x','y','r'])
cir = Circle(10,5,2)
# print(isinstance(cir, Circle))


q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
# print q

dd =defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
# print dd['key1']
# print dd['key2']

d = dict([('a',1),('b',2),('c',3)])
# print d
od = OrderedDict([('a',1),('b',2),('c',3)])
# print od

c = Counter()
for n in 'programmer':
	c[n] = c[n] + 1
# print c

# print base64.b64encode('abcd')
# print base64.b64decode('YWJjZA')
# print base64.urlsafe_b64decode('YWJjZA==')

md5 = hashlib.md5()
str = 'how to use md5 in python hashlib'
# md5.update(str)
# print md5.hexdigest()

md5.update('how to use md5')
md5.update(' in python hashlib')
# print md5.hexdigest()


sha1 = hashlib.sha1()
sha1.update(str)
print sha1.hexdigest()



























