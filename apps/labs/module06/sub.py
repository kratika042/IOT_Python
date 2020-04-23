import paho.mqtt.client as mqtt
from paho.mqtt import subscribe

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("topic/test",qos=1)
  client.unsubscribe()
  

def on_message(client, userdata, msg):
  if msg.payload.decode() == "Hello world!":
    print("Yes!")
    client.disconnect()
    
client = mqtt.Client()
client.connect("localhost",1883,60)

client.on_connect = on_connect
client.on_message = on_message
subscribe.simple(topics="topic/test", qos=1,hostname="abc", port=1883)
client.loop_forever()