'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
from labs.module03.TempSensorAdaptorTask import TempSensorAdaptorTask
from time import sleep
class TempSensorAdaptor():
    def __init__(self):     #constructor of TempSensorAdaptor 
        
        temp=TempSensorAdaptorTask("Thread")  #object of class TempSensorAdaptorTask is created
        '''
        Starting the thread
        '''
        temp.start()
        sleep(1)
       # temp.generateTemp()