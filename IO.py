#! usr/bin/env/python
# -*- coding: utf-8 -*-

import os
import json
import time,random

try:
	import cPickle as pickle
except ImportError:
	import pickle

str = '/Users/tanzhikang/personal/pythonProject/test.txt'

f = open(str,'w')
f.write('Hello world')
f.close()

with open(str) as f:
	for line in f.readlines():
		print(line.strip())

# print os.environ
# print os.getenv('PATH')
path = os.path.join(os.path.abspath('.'),'haha')
# print path

# print os.path.split(str)
# print os.path.splitext(str)

f = lambda x : x + ':haha'
# print [f(x) for x in os.listdir('.')]

pickleDict = dict(name='tanzhikang',age=26,height=172)
# print pickle.dumps(pickleDict)

f = open(str,'wb')
pickle.dump(pickleDict, f)
f.close()

f = open(str, 'rb')
d = pickle.load(f)
f.close()
# print d

# print json.dumps(d)
jsonStr = '{"name":"kangkang","age":26,"height":"172"}'
# print json.loads(jsonStr)

class Student(object):
	def __init__(self, name, age, job):
		self.name = name
		self.age = age
		self.job = job

ss = Student('kangkang', 26, 'programmer')


def StudentToJson(stu):
	return {
		'name':stu.name,
		'age':stu.age,
		'job':stu.job
	}

# print ss.__dict__
# print StudentToJson(ss)
# print(json.dumps(ss, default = StudentToJson))

def dict2Student(d):
	return Student(d['name'],d['age'],d['job'])

json_str = '{"age": 20, "job": "programmer", "name": "Bob"}'
result = json.loads(json_str, object_hook=dict2Student)
# print result.name


# print 'Process (%s) start ...' % os.getpid()
# pid = os.fork()
# if pid == 0:
# 	print 'i am sub process',os.getpid(),os.getppid()
# else:
# 	print 'i am main process',os.getpid(),pid


# from multiprocessing import Pool
# def long_time_task(name):
# 	# print 'Run task %s (%s)' % (name, os.getpid())
# 	start = time.time()
# 	time.sleep(random.random() * 3)
# 	end = time.time()
# 	# print 'Task %s runs %0.2f sec' % (name, (end - start))

# if __name__ == '__main__':
# 	print 'Parent process %s.' % os.getpid()
# 	p = Pool(5)
# 	for n in range(5):
# 		p.apply_async(long_time_task, args = (n,))
# 	# print 'Waiting for all subprocess done...'
# 	p.close()
# 	p.join()
# 	# print 'All process has done'


from multiprocessing import Process,Queue
import os,time,random

def write(q):
	for value in ['A','B','C']:
		print 'Put %s into queue' % value
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		value = q.get(True)
		print 'Get %s from queue.' % value

if __name__ == '__main__':
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()














