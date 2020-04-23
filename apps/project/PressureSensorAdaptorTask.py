'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''

from sense_hat import SenseHat
import logging
from threading import Thread
from time import sleep
import time

from project.UbidotsClientConnector import ubidots
import paho.mqtt.client as mqttClient
from labs.common.SensorData import SensorData
from project.MultiActuatorAdaptor import MultiActuatorAdaptor
from project.SensorDataManager import SensorDataManager
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.common.ConfigUtil import ConfigUtil

logger = logging.getLogger('default')
logging.basicConfig(level=logging.INFO, format='%(message)s')
class PressureSensorAdaptorTask(Thread):
    '''
    Variables are defined and objects of required classes are created with the class scope.
    '''
    sensorData=SensorData()         #constructor of sensorData is created.
   # multiAct=MultiActuatorAdaptor()   #constructor of TempActuatorAdaptor is created.
    sensorDataM=SensorDataManager() #constructor of SensorDataManager is created.
    avgValue=0.0
    count=0.0
    total=0.0
    currentValue=0.0
    maxValue=0.0
    minValue=0.0
    timestamp=None
    sh=SenseHat() 
    def __init__(self,name):        #constructor is initialized
        Thread.__init__(self)
        self.name=name
    '''
    this run function overrides the run function of Thread and calls the sense hat function to generate the Pressure values,addValue fnctn of sensorData is called
    pressure of class sensorDataManager is called and sensorData object is passed as a parameter.
    This function will return the actuator data.
    '''    
        
    def run(self):              #run method of thread is overriden
       # logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
        sh = SenseHat()
        mqtt_client = mqttClient.Client()
        while True:
            res = sh.get_pressure()
            self.sensorData.addValue(res)
            self.act_data=self.sensorDataM.pressure(self.sensorData)
            self.getSensorData()
            ubidots(mqtt_client,self.currentValue,"pressure")
            time.sleep(2)
#         if(self.act_data!=None):
#             self.multiAct.updateActuator(self.act_data)      #calling of updateActuator
#         
#         logging.basicConfig(level=logging.INFO)
#         data="Pressure Sensor:\nTime:    "+str(self.timestamp)+"\nCurrent:    "+str(self.currentValue)+"\nAverage:    "+str(self.avgValue)+"\nSamples:    "+str(self.count)+"\nMin:    "+str(self.minValue)+"\nMax:    "+str(self.maxValue)    
#         logging.info(data)
#         print("\n")
#     
    '''
    This function fetches the values from sensorData and store it to the local variables of this class.
    '''  
    def getSensorData(self):
        self.avgValue= self.sensorData.getAverageValue();
        self.count=self.sensorData.getCount();
        self.total=self.sensorData.getTotal();
        self.currentValue=self.sensorData.getCurrentValue();
        self.maxValue=self.sensorData.getMaxValue();
        self.minValue=self.sensorData.getMinValue();
        self.timestamp=self.sensorData.getTimestamp();