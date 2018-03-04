#! /usr/bin/python

import itertools

natuals = itertools.count(1)
natualResult = itertools.takewhile(lambda x : x <= 10, natuals)

# for nn in natualResult:
	# print nn

# for n in natuals:
# 	print n


# ns = itertools.repeat('A',10)
# for s in ns:
# 	print s

# for c in itertools.chain('ABC','XYZ'):
# 	print c

for k,v in itertools.groupby('AAABBBCCAAA'):
	print k,list(v)