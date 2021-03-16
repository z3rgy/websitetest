import os

from flask import Flask, render_template, request, session, escape
 
import mysql 
import mysql.connector
dbconfig={'host':'localhost','user':'root','password':'','database':'member_db'}
conn=mysql.connector.connect(**dbconfig)
cursor=conn.cursor()
SQL = '''SELECT * FROM login_t'''
cursor.execute(SQL)
alldata = cursor.fetchall()
a=0
p_id='jack1'
for i in alldata:
 name=alldata[a][0]
 a =a + 1
 if name == p_id:
  print('name:',name)
  print('p_id:',p_id)
 else:
  pass