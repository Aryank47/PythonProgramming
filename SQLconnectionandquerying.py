# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 15:13:39 2019

@author: Aryan Kumar
"""


import mysql.connector as ms

mydb=ms.connect(
    host="localhost",
    user="root",
    passwd="1qazxsw2",
    database="aryan"
)
cur = mydb.cursor()

cur.execute('select *from student')
for result in cur:
    print(result)

cur.close()
mydb.close()