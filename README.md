本项目为自己的毕业设计
使用mqtt协议进行数据的传递，穿透内网，通过linux端接收、保存并且展示数据，简单的数据报格式和简单的传递方式。
centos是服务器端的设计
esp8266是mcu端的设计
其中，index.php中使用了百度的图表制作源



===================================================================================================
# 一、先使用linux服务器搭建mqtt服务 #

wget http://emqtt.com/downloads/3006/centos7  //先下载emqttd \n
安装emqttd具体请看 http://emqtt.com/docs/v2/install.html

# 二、使用linux服务器搭建收集程序 #

安装python3
安装pip3
使用pip3 安装paho.mqtt
# 三、使用过程 #

1.将esp8266烧写成支持micropython的固件
2.使用micropython编写发送端
3.服务器端开启emqtt，并且在服务器编写监听程序
4.监听程序保存至数据库
5.安装php、apache、mariadb等并且连接数据库等
6.展示

  
  ===================================================================================================
  
  
![00.png](https://i.loli.net/2018/11/01/5bda921355445.png)
![01.png](https://i.loli.net/2018/11/01/5bda92384dd89.png)


完成的展示图片如图
