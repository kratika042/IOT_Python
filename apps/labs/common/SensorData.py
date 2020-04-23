'''
Created on Jan 26, 2020

@author: Kratika Maheshwari
'''
from _datetime import datetime
class SensorData:
    
    timestamp=None
    name="Temperature"
    currentValue=0.0
    averageValue=0.0
    minValue=0.0
    maxValue=0.0
    total=0.0
    count=0.0
    
    def __init__(self):
        self.timestamp=str(datetime.now())
        
    ''' 
    Temperature value is passed to this function and all the variables are calculated.
    '''    
    def addValue(self,val):
        print(val)
        self.count+=1
        self.timestamp=str(datetime.now())
        self.total+=val
        self.currentValue=val
        
        if(val<self.minValue):
            self.minValue=val
        if(val>self.maxValue):
            self.maxValue=val
        if(self.count>0 and self.total!=0):
            self.averageValue=self.total/self.count
            
    '''
    Getter functions to fetch all the variables.
    '''        
    def getAverageValue(self):
        return self.averageValue
    def getCount(self):
        return self.count
    def getCurrentValue(self):
        return self.currentValue
    def getMaxValue(self):
        return self.maxValue
    def getMinValue(self):
        return self.minValue
    def getName(self):
        return self.name
    def getTimestamp(self):
        return self.timestamp
    def getTotal(self):
        return self.total
    