#! /usr/bin/python
# -*- coding: utf-8 -*-
import time
import paho.mqtt.subscribe as subscribe
import re
import pymysql

def sjk():
	db = pymysql.connect("localhost","****","******","BYSJ")
	return db
def xrsj(a):
	db = sjk()
	cursor = db.cursor()
	cursor.execute('insert into bysj values("%d","%d","%d")'%(a[0],a[1],a[2]))
	db.commit()
	db.close
def int_c(msg):
	ss = str(msg)
	s = re.findall(r'\d+\.?d*',ss)
	res1 = int(s[0])
	res2 = int(s[1])
	res3 = int(s[2])
	res4 = int(s[3])
	return (res1,res2,res3,res4)

def sub():
	msg = subscribe.simple("bysj", hostname="www.wangyaominde.cn",client_id="server")
	a = int_c(msg.payload)
	return a

while True:
	a=sub()
	if(a[3]==1):
		fire = "fire"
	else:
		fire = "no fire"

	xrsj(a)
	print("wendu is :%d\tshidu is : %d\nmq is : %d\t%s"%(a[0],a[1],a[2],fire))
