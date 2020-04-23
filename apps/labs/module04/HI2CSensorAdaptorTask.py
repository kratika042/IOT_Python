'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''
import numpy
from threading import Thread
import smbus
from time import sleep
import logging
from sense_hat import SenseHat
from labs.common.SensorData import SensorData
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
from labs.module03.SensorDataManager import SensorDataManager

i2cBus = smbus.SMBus(1)
logger = logging.getLogger('default')
logging.basicConfig(level=logging.INFO, format='%(message)s')


class HI2CSensorAdaptorTask(Thread):
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
   
    def __init__(self,name):        #constructor is called
        Thread.__init__(self)
        self.name=name

    '''
    this run function overrides the run function of Thread and calculates the Humidity values from the I2C bus,addValue fnctn of sensorData is called
    humidityI2C of class sensorDataManager is called and sensorData object is passed as a parameter.
    This function will return the actuator data.
     
    '''
    def run(self):
        logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
        
        while True:
        
            lsb1 =i2cBus.read_byte_data(0x5f,0x36)
            msb1 =i2cBus.read_byte_data(0x5f,0x37)
            H0 = numpy.int16((msb1<<8)|lsb1)
            
            lsb2 =i2cBus.read_byte_data(0x5f,0x3A)
            msb2 =i2cBus.read_byte_data(0x5f,0x3B)
            H1 = numpy.int16((msb2<<8)|lsb2)
            
            lsb3 =i2cBus.read_byte_data(0x5f,0x28)
            msb3 =i2cBus.read_byte_data(0x5f,0x29)
            H = numpy.int16((msb3<<8)|lsb3)
            
            h1=numpy.uint16(i2cBus.read_byte_data(0x5f, 0x31)>>1)
            h0=numpy.uint16(i2cBus.read_byte_data(0x5f, 0x30)>>1)
            
            per= ((h1 - h0) * (H-H0)/(H1-H0))+h0
            self.sensorData.addValue(per)
            self.act_data=self.sensorDataM.humidityI2C(self.sensorData)
            self.getSensorData()
            if(self.act_data!=None):
                self.multiAct.updateActuator(self.act_data)
           # logger.info("I2C: " +str(per)+"%" )
            logging.basicConfig(level=logging.INFO)
            data="HI2C Sensor:\nTime:    "+str(self.timestamp)+"\nCurrent:    "+str(self.currentValue)+"\nAverage:    "+str(self.avgValue)+"\nSamples:    "+str(self.count)+"\nMin:    "+str(self.minValue)+"\nMax:    "+str(self.maxValue)    
            logging.info(data)
            print("\n")
        return None   
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
