'''
Created on Mar 13, 2020

@author: Kratika Maheshwari
'''
import paho.mqtt.client as mqtt
from paho.mqtt import publish

# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/test", "Hello world!");
#publish.single("topic/test", payload=None, qos=2,hostname= "user", port=1883)

client.disconnect()