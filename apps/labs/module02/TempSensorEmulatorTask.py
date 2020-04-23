'''
Created on Jan 26, 2020

@author: Kratika Maheshwari
'''
from labs.common.SensorData import SensorData
import logging
from labs.module02.SmtpClientConnector import SmtpClientConnector
#from random import random, randrange
import random
import time


class TempSensorEmulatorTask:
    sensorObj=SensorData()
    currentValue=0.0
    total=0.0
    count=0.0
    minValue=0.0
    maxValue=0.0
    avgValue=0.0
    threshold=5.0
    timestamp=None
    ''' Email will be sent according to the difference in current and average temperature values
        logging info is also generated.
    '''
    
    def sendNotification(self):
        if(abs(self.currentValue-self.avgValue)>self.threshold):
            smtpCCObject=SmtpClientConnector()
            smtpCCObject.connector()
            logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
            logging.info('\n Current temperature exceeds average by ' + str(round(abs(self.currentValue-self.avgValue),2)) + '. Triggering alert...')
            
        
        
        logging.basicConfig(level=logging.INFO)
        data="Temperature:\nTime:    "+str(self.timestamp)+"\nCurrent:    "+str(self.currentValue)+"\nAverage:    "+str(self.avgValue)+"\nSamples:    "+str(self.count)+"\nMin:    "+str(self.minValue)+"\nMax:    "+str(self.maxValue)    
        logging.info(data)
        print("\n")
            
    ''' fetch data from SensorData class, hence create an object of that class and fetch the variables using 
        getter functions.
    '''
    def getSensorData(self):
        self.avgValue= self.sensorObj.getAverageValue();
        self.count=self.sensorObj.getCount();
        self.total=self.sensorObj.getTotal();
        self.currentValue=self.sensorObj.getCurrentValue();
        self.maxValue=self.sensorObj.getMaxValue();
        self.minValue=self.sensorObj.getMinValue();
        self.timestamp=self.sensorObj.getTimestamp();
        return self.sensorObj
    
    '''
    Random temperature value is generated and it is passed in the addValue function of SensorData class.
    After getting all the values sendNotification function is called and thread is sleep for 2 seconds.
    '''
    def temperatureGenerator(self):
        for i in range(0,10):
            temperatureValue=random.uniform(0,30)
            self.sensorObj.addValue(temperatureValue)
            self.getSensorData()
            self.sendNotification()
            time.sleep(2) 