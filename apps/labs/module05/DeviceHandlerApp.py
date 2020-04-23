'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
import os.path,subprocess
import os
from py4j.java_gateway import JavaGateway
from subprocess import STDOUT,PIPE
from labs.module05.TempSensorAdaptor import TempSensorAdaptor

class DeviceHandlerApp():
    def __init__(self):
        '''
        Object of class TempSensorAdaptor is created.
        '''     
      
        tempSense=TempSensorAdaptor()  
        
if __name__=='__main__':
     
     DeviceHandlerApp()    