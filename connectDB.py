#! /usr/bin/python

import mysql.connector
 
conn = mysql.connector.connect(
         user='root',
         password='123456789',
         host='127.0.0.1',
         database='DBHAHA',
         use_unicode=True)
 
cur = conn.cursor()
 

query = 'select * from user'
 

cur.execute(query)
 
for (id, name) in cur:
    print("{}, {}".format(id, name))
 