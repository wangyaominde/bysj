import network
from mqtt import MQTTClient 
import dht
import machine 
import time 

 
def sub_cb(topic, msg): 
   print(msg) 

   
   
#====================connect wifi===============================#
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("wifiname","wifipass")
 
while not sta_if.isconnected():  
    machine.idle() 
print("Connected to Wifi\n") 








'''#=======================flame======================#
flame = machine.Pin(16, machine.Pin.IN)
while True:
	if(flame.value() == 0):
		print("fire")
	else:
		print("no fire")
	time.sleep(1)




#===================dht11=========================================#
d = dht.DHT11(machine.Pin(2))
while True:
	d.measure()		#celiang
#	d.temperature()    # wendu
#	d.humidity()		#shidu
	print("wendu is %d shidu is %d"%(d.temperature(),d.humidity()))
	time.sleep(1)

 
 
 
 '''
#==========================mqtt===============================#
client = MQTTClient("client_name", "mqttserver",port=<portnum>) 
client.set_callback(sub_cb) 
client.connect()
#client.subscribe(topic="bysj") 
d = dht.DHT11(machine.Pin(2))
flame = machine.Pin(16, machine.Pin.IN)
mq = machine.ADC(0)
while True: 
	d.measure()
	if(flame.value() == 0):
		client.publish(topic = "bysj",msg = "%d %d %d 1"%(d.temperature(),d.humidity(),mq.read()))
	else:
		client.publish(topic = "bysj",msg = "%d %d %d 0"%(d.temperature(),d.humidity(),mq.read()))
	time.sleep(1)
#    print("Sending ON")
'''	if(flame.value() == 0):
		client.publish(topic = "bysj/fire", msg = "fire")
	else:
		client.publish(topic = "bysj/fire", msg = "no fire")
	client.publish(topic = "bysj/wendu",msg = "%d"%d.temperature())
	client.publish(topic = "bysj/shidu",msg = "%d"%d.humidity())
	client.publish(topic = "bysj/mq",msg = "%d"%mq.read())
	print("Sending OFF") 
	client.publish(topic="bysj", msg="0")
	time.sleep(1) '''