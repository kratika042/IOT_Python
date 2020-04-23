'''
Created on Mar 4, 2020

@author: Kratika Maheshwari
'''
import paho.mqtt.client as mqtt
import json
from labs.module05.DataUtil import DataUtil
from labs.common.SensorData import SensorData
MQTT_Host="127.0.0.1"
MQTT_Port=1883
MQTT_KeepAlive=10
du=DataUtil()
sd=SensorData()

mqttc=mqtt.Client()
class MqttClientConnector():
    def __init__(self):
        mqttc.connect(MQTT_Host,MQTT_Port,MQTT_KeepAlive)
        print("MQTT Session established")
    def publish_sensor_data(self,mqtt_topic,sd):
        mqtt_msg=du.toJsonFromSensorData(sd) 
        print(mqtt_msg)
        mqttc.publish(mqtt_topic,mqtt_msg) 
    def subscribe_actuator(self):
        mqttc.subscribe("ActuatorData")
    def on_received_actuator_data(self,client,userdata,msg):
        print(msg.topic)
        print(msg.payload)   
               
        
def on_publish(mqttc,userdata,res):
        print("Data published")        
def on_message(client,userdata,msg):
        print("here")
        print("msg rcvd", str(msg.payload.decode()))
        print("msg topic=",msg.topic)
        print("qos=",msg.qos)
        print("flag=",msg.retain)
def on_connect(mqttc,userdata,flags,rc):
    mqttc.loop_forever()
    print("connection ok") 
    
mqttc.on_publish=on_publish
mqttc.on_connect=on_connect  
  
mqttc.on_message=on_message 
mqtt_topic="mytopic"
mqttc.publish(topic=mqtt_topic,qos=2) 
mq=MqttClientConnector()
mq.publish_sensor_data(mqtt_topic, sd)
            