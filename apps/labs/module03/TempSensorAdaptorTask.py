'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
from labs.common.SensorData import SensorData
from labs.module03.SensorDataManager import SensorDataManager
from labs.common.ConfigUtil import  ConfigUtil
from labs.module03.TempActuatorAdaptor import TempActuatorAdaptor
import labs.module02.SmtpClientConnector as SmtpClientConnector
from labs.module08.UbidotsClientConnector import ubidots
import logging
import time

import paho.mqtt.client as mqttClient
import random
from sense_hat import SenseHat
from threading import Thread
class TempSensorAdaptorTask(Thread):
    '''
    Variables are defined and objects of required classes are created with the class scope.
    '''
    
    sensorData=SensorData()         #constructor of sensorData is created.
    tempAct=TempActuatorAdaptor()   #constructor of TempActuatorAdaptor is created.
    sensorDataM=SensorDataManager() #constructor of SensorDataManager is created.
    smtpCCObject=SmtpClientConnector.SmtpClientConnector()  ##constructor of SmtpClientConnector is created.
    confP=ConfigUtil()  #constructor of ConfigUtil is created.
    avgValue=0.0
    count=0.0
    total=0.0
    currentValue=0.0
    maxValue=0.0
    minValue=0.0
    timestamp=None
    sh=SenseHat()       #constructor of SenseHat is created.
    '''
    nominal temperature is fetched from configuration file using object of ConfigParser.
    '''
    nominal=confP.getValue("device", "nominalTemp")
    print("im nominal",nominal)
    '''
    constructor of class TempSensorAdaptorTask
    '''
    def __init__(self,name):
       # self.generateTemp()
        Thread.__init__(self);
        self.name=name
    '''
    this run function overrides the run function of Thread and calls the sense hat function to generate the temperature values,addValue fnctn of sensorData is called
    handleSensorData of class sensorDataManager is called and sensorData object is passed as a parameter.
    This function will return the actuator data. notification fucn will be called to check the condition of sending the email
    '''
    
    def run(self):
        #for i in range(0,10):
       # while True:
        
        mqtt_client = mqttClient.Client()
        while True:
            self.val=self.sh.get_temperature()      #calling get_temperature function
            
            self.sensorData.addValue(self.val)  #calling addValue function of sensorData
            self.act_data=self.sensorDataM.handleSensorData(self.sensorData)
            self.getSensorData()
            
           #commented out for mod8# self.sendNotification(self.act_data.getCommand(), self.act_data.getValue(),self.nominal)
            
            ubidots(mqtt_client,self.avgValue,self.currentValue)
            time.sleep(2)
          #mod8#  if(self.act_data!=None):
            #mod8#    self.tempAct.updateActuator(self.act_data)      #calling of updateActuator
            #mod8# time.sleep(2)    
     #   return None    
    '''
    values of sensor data is fetched to store in local variables.
    '''        
    def getSensorData(self):
        self.avgValue= self.sensorData.getAverageValue();
        self.count=self.sensorData.getCount();
        self.total=self.sensorData.getTotal();
        self.currentValue=self.sensorData.getCurrentValue();
        self.maxValue=self.sensorData.getMaxValue();
        self.minValue=self.sensorData.getMinValue();
        self.timestamp=self.sensorData.getTimestamp();
                
    '''
    notification regarding email alert and logging information is handled by sendNotification function, it takes 3 arguments
    namely command which is set to actuator data, current Temperature value and the nominal value
    '''            
    def sendNotification(self,command,current,nominal): 
        logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
        nominal=float(nominal)     
        if(command=="TEMP INC"):
            logging.info('\n Current temperature exceeds Nominal Temperature by ' + str(round(abs(current-nominal),2)) + '. Triggering alert...')
        elif(command=="TEMP DEC"):
            logging.info('\n Current temperature deceeds Nominal Temperature by ' + str(round(abs(current-nominal),2)) + '. Triggering alert...')    
        else:
            logging.info('\n Current temperature is neutral to Nominal Temperature')    
        
      #  self.smtpCCObject.connector(command)
        logging.basicConfig(level=logging.INFO)
        data="Temperature:\nTime:    "+str(self.timestamp)+"\nCurrent:    "+str(self.currentValue)+"\nAverage:    "+str(self.avgValue)+"\nSamples:    "+str(self.count)+"\nMin:    "+str(self.minValue)+"\nMax:    "+str(self.maxValue)    
        logging.info(data)
        print("\n")
    