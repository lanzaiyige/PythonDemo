#! /usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('192.168.1.106',8888))

print('bind port 8888')

while True:
	data, addr = s.recvfrom(1024)
	print('receive %s:%s' % (data,addr))
	s.sendto('this %s' % data.decode('utf-8'), addr)