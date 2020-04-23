'''
Created on Jan 26, 2020

@author: Kratika Maheshwari
'''
''' In constructor, object of TempSensorEmulatorTask is created and temperatureGenerator function is called.  '''

from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
class TempEmulatorAdaptor:
    def __init__(self):         #constructor of TempEmulatorAdaptor 
        tempSensor=TempSensorEmulatorTask() #object of TempSensorEmulatorTask is created
        tempSensor.temperatureGenerator()   #temperatureGenerator function is called