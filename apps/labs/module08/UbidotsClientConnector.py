'''
Created on Mar 22, 2020

@author: Kratika Maheshwari
'''
from labs.module03 import TempSensorAdaptorTask
'''
This Example sends harcoded data to Ubidots using the Paho MQTT
library.

Please install the library using pip install paho-mqtt


'''
import paho.mqtt.client as mqttClient
import time
import json
import random
'''
global variables
'''

connected = False  # Stores the connection status
BROKER_ENDPOINT = "things.ubidots.com"
PORT = 1883
MQTT_USERNAME = "BBFF-08hJyBD6jtjlrxddzfS6pmyGfgMgX8"  # Put your TOKEN here
MQTT_PASSWORD = ""
TOPIC = "/v1.6/devices/"
DEVICE_LABEL = "temperature-sensor"
VARIABLE_LABEL = "currenttemp"
VARIABLE_LABEL2="averagetemp"


'''
Functions to process incoming and outgoing streaming
'''


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("[INFO] Connected to broker")
        global connected  # Use global variable
        connected = True  # Signal connection

    else:
        print("[INFO] Error, connection failed")

'''
displays output when data is published
'''
def on_publish(client, userdata, result):
    print("[INFO] Published!")

'''
connect to the ubidots client 
'''
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not connected:
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Waits for connection
            print("[INFO] Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True

'''
publish the payload to the specified topic
'''
def publish(mqtt_client, topic, payload):
    try:
        mqtt_client.publish(topic, payload)
    except Exception as e:
        print("[ERROR] There was an error, details: \n{}".format(e))


'''
mqtt client connects with the ubidots cloud and send the data(payload) to connect method
'''
def ubidots(mqtt_client,avgVal,curVal):
   
    payload={VARIABLE_LABEL: curVal, VARIABLE_LABEL2:avgVal}
    payload = json.dumps(payload)
    topic = "{}{}".format(TOPIC, DEVICE_LABEL)
 
    if not connected:  # Connects to the broker
        connect(mqtt_client, MQTT_USERNAME, MQTT_PASSWORD,
                BROKER_ENDPOINT, PORT)
 
    # Publishes values
    print("[INFO] Attempting to publish payload:")
    print(payload)
    publish(mqtt_client, topic, payload)

