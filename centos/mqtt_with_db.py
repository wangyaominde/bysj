#! /usr/bin/python
# -*- coding: utf-8 -*-
import time
import paho.mqtt.subscribe as subscribe
import re
import pymysql

def sjk():
	db = pymysql.connect("localhost","****","******","BYSJ")  #链接数据库
	return db
def xrsj(a):
	db = sjk()
	cursor = db.cursor()
	cursor.execute('insert into bysj values("%d","%d","%d")'%(a[0],a[1],a[2]))  #将温湿度和空气质量保存至数据库
	db.commit()
	db.close
def int_c(msg):
	ss = str(msg)
	s = re.findall(r'\d+\.?d*',ss)   #拿到有用的数据
	res1 = int(s[0])
	res2 = int(s[1])
	res3 = int(s[2])
	res4 = int(s[3])
	return (res1,res2,res3,res4)

def sub():
	msg = subscribe.simple("bysj", hostname="www.wangyaominde.cn",client_id="server")  #开启mqtt订阅
	a = int_c(msg.payload)
	return a

while True:
	a=sub()
	if(a[3]==1):
		fire = "fire"	#是否有火焰
	else:
		fire = "no fire"

	xrsj(a)
	print("wendu is :%d\tshidu is : %d\nmq is : %d\t%s"%(a[0],a[1],a[2],fire))	#屏幕输出，调试用，后台可看
