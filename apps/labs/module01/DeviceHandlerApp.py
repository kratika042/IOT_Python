'''
Created on Jan 19, 2020

@author: Kratika Maheshwari
'''
#import psutil
from labs.module01.SystemPerformanceAdaptor import SystemPerformanceAdaptor
'''
This class initializes SystemPerformaceAdaptor. 
Here, object of SystemPerformanceAdaptor class is created and util() function is called.
'''
class DeviceHandlerApp():
    def handle(self):
        sysPerformance=SystemPerformanceAdaptor();
        sysPerformance.util()       #util() function is called by the object of class SystemPerformanceAdaptor
obj=DeviceHandlerApp()              #object of class DeviceHandlerApp is created
obj.handle()                        #object calls the function handle()
    