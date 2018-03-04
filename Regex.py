#! /usr/bin/python
# -*- coding: UTF-8 -*-

import re
# str = '14:40:23'
# str = '1023000'
# str = 'someone@hotmail.com'
str = 'bill.gates@microsoft.com'

# reg = r'^(\d{3})-(\d{3,8})$'
# reg = r'^(0[0-9]|1[0-9]|2[0-3])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9][0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9][0-9])$'
# reg = r'^(\d+?)(0*)$'
reg = r'^[0-9a-zA-z.]+@[\d\w]+.com$'

result = re.match(reg, str)
if(result):
	print 'OK'
else:
	print 'Fail'

# print(result.group(1))
# print(result.group(2))

# print(re.split(r':', str))
# print('ab  i  p'.split(' '))
# print(re.split(r'\s+','a  , b  ,  c'))
# print(re.split(r'[\s,]+', 'a ,  b, c'))

