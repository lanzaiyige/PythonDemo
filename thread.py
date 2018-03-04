import time,threading,multiprocessing

if 0:
	def loop():
		print 'thread %s is running' % threading.current_thread().name
		n = 0
		while n < 5:
			n = n + 1
			print 'thread %s >>> %s' % (threading.current_thread().name, n)
			time.sleep(1)
		print 'thread %s ended.' % threading.current_thread().name


	print 'thread %s is running...' % threading.current_thread().name
	t = threading.Thread(target=loop, name='LoopThread')
	t.start()
	t.join()
	print 'thread %s ended.' % threading.current_thread().name

balance = 0
lock = threading.Lock()

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

def run_thread(n):
	for n in range(100000):
		lock.acquire()
		try:
			change_it(n)
		finally:
			lock.release()
		

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print balance


# def loop():
# 	x = 0
# 	while True:
# 		x = x ^ 1

# for n in range(multiprocessing.cpu_count()):
# 	t = threading.Thread(target=loop)
# 	t.start()

# local_school = threading.local()

# def process_student():
# 	print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

# def process_thread(name):
# 	local_school.student = name
# 	process_student()

# t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target=process_thread, args=('Tom',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

thread_download = threading.local()

def threadDownload(url, fileName):
	thread_download.url = url
	thread_download.fileName = fileName
	print 'downloading %s' % url

t1 = threading.Thread(target=threadDownload, args=('htts://www.baidu.com','baidu'),name='baiduThread')
t2 = threading.Thread(target=threadDownload, args=('htts://www.google.com','baidu'),name='googleThread')
t1.start()
t2.start()
t1.join()
t2.join()

















