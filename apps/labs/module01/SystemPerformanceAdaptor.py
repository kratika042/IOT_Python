'''
Created on Jan 19, 2020

@author: Kratika Maheshwari
'''
#import psutil
import logging
from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask
class SystemPerformanceAdaptor(object):
    '''
    util() function of SystemPerformanceAdaptor class manages the calling of CPU and Memory Utilization.
    this function is calling getDataFromSensor function of SystemCpuUtilTask and SystemMemUtilTask 10 times to get the 10 records 
    of the CPU and Memory Utilization with the interval of 2 seconds.
    Logger is set with the level=logging.INFO
    '''
    def util(self):
        for i in range(10):                    #loop for calling function 10 times to 10 the 10 log outputs.
            sysCpu=SystemCpuUtilTask();         #object of SystemCpuUtilTask is created 
            cpuUtil=sysCpu.getDataFromSensor()  #function is called
            sysMem=SystemMemUtilTask()          #object of SystemMemUtilTask is created 
            memUtil=sysMem.getDataFromSensor()  #function is called
            logging.basicConfig(level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
            data='CPU Utilization='+str(cpuUtil)
            logging.info(data)                  #CPU data is logged
            data='Memory Utilization='+str(memUtil)
            logging.info(data)                  # Memory data is logged.
