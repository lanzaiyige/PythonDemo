#! /usr/bin/python

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2

class PyEventParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self._count = 0
		self._events = dict()
		self._flag = None

	def handle_starttag(self, tag, atts):
		if tag == 'h3' and atts.__contains__(('class','event-title')):
			self._count += 1
			self._events[self._count] = dict()
			self._flag