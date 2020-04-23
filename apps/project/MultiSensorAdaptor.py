'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''
from project.TempSensorAdaptorTask import TempSensorAdaptorTask
from project.HumiditySensorAdaptorTask import HumiditySensorAdaptorTask
from project.PressureSensorAdaptorTask import  PressureSensorAdaptorTask
import threading
class MultiSensorAdaptor():
    def __init__(self):     #constructor of TempSensorAdaptor 
        
        
        '''
        Starting the threads for all the three classes of sensors 
        '''
        while True:
            temp=TempSensorAdaptorTask("Temp Sensor")  #object of class TempSensorAdaptorTask is created
            humidity1=HumiditySensorAdaptorTask("Humidity sensor")  #object of class HumiditySensorAdaptorTask is created
            pressure=PressureSensorAdaptorTask("Pressure Sensor")
            temp.start()        #Thread is started
            humidity1.start()       #Thread is started
            pressure.start()
            temp.join()         #Thread is put on wait until it finishes
            humidity1.join()        #Thread is put on wait until it finishes
            pressure.join()
            