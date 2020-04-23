'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from labs.module04.HI2CSensorAdaptorTask import HI2CSensorAdaptorTask

from labs.module04.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
class MultiSensorAdaptor():
    def __init__(self):     #constructor of TempSensorAdaptor 
        
        
        '''
        Starting the threads for all the three classes of sensors 
        '''
        while True:
            temp=TempSensorAdaptorTask("Temp Sensor")  #object of class TempSensorAdaptorTask is created
            humidity1=HumiditySensorAdaptorTask("Humidity sensor")  #object of class HumiditySensorAdaptorTask is created
            humidity2=HI2CSensorAdaptorTask("I2C Sensor")   #object of class HI2CSensorAdaptorTask is created
            temp.start()        #Thread is started
            temp.join()         #Thread is put on wait until it finishes
           
            humidity1.start()       #Thread is started
            humidity1.join()        #Thread is put on wait until it finishes
          
            humidity2.start()       #Thread is started
            humidity2.join()        #Thread is put on wait until it finishes
        