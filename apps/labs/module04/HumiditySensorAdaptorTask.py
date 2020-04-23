'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''

from sense_hat import SenseHat
import logging
import smbus
from threading import Thread
from time import sleep
from labs.common.SensorData import SensorData
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.module03.SensorDataManager import SensorDataManager
from labs.module02.SmtpClientConnector import SmtpClientConnector
from labs.common.ConfigUtil import ConfigUtil
i2cBus = smbus.SMBus(1)
logger = logging.getLogger('default')
logging.basicConfig(level=logging.INFO, format='%(message)s')
class HumiditySensorAdaptorTask(Thread):
    '''
    Variables are defined and objects of required classes are created with the class scope.
    '''
    sensorData=SensorData()         #constructor of sensorData is created.
    multiAct=MultiActuatorAdaptor()   #constructor of TempActuatorAdaptor is created.
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
    this run function overrides the run function of Thread and calls the sense hat function to generate the Humidity values,addValue fnctn of sensorData is called
    humidity of class sensorDataManager is called and sensorData object is passed as a parameter.
    This function will return the actuator data.
    '''    
        
    def run(self):              #run method of thread is overriden
        logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
        sh = SenseHat()
        res = sh.get_humidity()
        self.sensorData.addValue(res)
        self.act_data=self.sensorDataM.humidity(self.sensorData)
        self.getSensorData()
        if(self.act_data!=None):
            self.multiAct.updateActuator(self.act_data)      #calling of updateActuator
        
        logging.basicConfig(level=logging.INFO)
        data="Humidity Sensor:\nTime:    "+str(self.timestamp)+"\nCurrent:    "+str(self.currentValue)+"\nAverage:    "+str(self.avgValue)+"\nSamples:    "+str(self.count)+"\nMin:    "+str(self.minValue)+"\nMax:    "+str(self.maxValue)    
        logging.info(data)
        print("\n")
    
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