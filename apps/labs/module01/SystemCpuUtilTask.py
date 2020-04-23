'''
Created on Jan 19, 2020

@author: Kratika Maheshwari
'''
import psutil
class SystemCpuUtilTask():
    '''
    getDataFromSensor() function of SystemCpuUtilTask class returns the average CPU Utilization of the system 
    with the interval of 2 seconds.
    '''
    def getDataFromSensor(self):
        return(psutil.cpu_percent(interval=2))    #CPU utilization is calculated using psutil library.
    
    

        
        
        