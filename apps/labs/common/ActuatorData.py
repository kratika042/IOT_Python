'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
'''
This class contains the getter and setter methods for Actuator data.
'''

class ActuatorData():
    command="Null"    #command is initialized with null.
    currentVal=0.0      #currentVal is initialized with 0.0
    name="Temperature"         #name is initialized with Temperature
    '''
    getters and setters for all the variables of class ActuatorData.
    '''
    
    def getCommand(self):
        return self.command
    def getValue(self):
        return self.currentVal
    def getName(self):
        return self.name
    def setCommand(self,cmnd):
        self.command=cmnd
    def setName(self,sensorName):
        self.name=sensorName
    def setValue(self,value):
        self.currentVal=value
        