'''
Created on Jan 19, 2020

@author: Kratika Maheshwari
'''
import psutil;
class SystemMemUtilTask():
    '''
     getDataFromSensor() function of SystemMemUtilTask class returns the average Physical Memory Utilization of the system in percentage
    '''
    def getDataFromSensor(self):
        return(psutil.virtual_memory().percent)      #Memory Utilization is calculated using psutil library.
    