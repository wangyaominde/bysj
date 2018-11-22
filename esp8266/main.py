import network
from mqtt import MQTTClient
import dht
import machine
import time


def sub_cb(topic, msg): #回调函数
   print(msg)


#====================connect wifi===============================#
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("wifiname","wifipass")    #输入wifi的账号密码

while not sta_if.isconnected():     #判断是否连接成功
    machine.idle()
print("Connected to Wifi\n")


#==========================mqtt===============================#
client = MQTTClient("client_name", "mqttserver",port=<portnum>)     #mqtt服务器配置，“客户端的名字”，“mqtt服务器地址”，"mqtt端口号"
client.set_callback(sub_cb)     #设置回调函数为在屏幕输出当前的值，用来调试和验证程序
client.connect()        #连接mqtt服务器
#client.subscribe(topic="bysj")     #之前调试用，现已弃置
d = dht.DHT11(machine.Pin(2))   #获取dht11的数值
flame = machine.Pin(16, machine.Pin.IN) #获取火焰传感器的值
mq = machine.ADC(0) #获取mq空气质量传感器的值，并且进行ad转换
while True:
	d.measure()    #测量一次dht11
	if(flame.value() == 0):
		client.publish(topic = "bysj",msg = "%d %d %d 1"%(d.temperature(),d.humidity(),mq.read()))    #向主题为：‘bysj’ 发送“温度，湿度，空气质量”
	else:
		client.publish(topic = "bysj",msg = "%d %d %d 0"%(d.temperature(),d.humidity(),mq.read()))     #向主题为：‘bysj’ 发送“温度，湿度，空气质量”
	time.sleep(1)
