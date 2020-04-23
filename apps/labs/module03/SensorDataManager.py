'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
from sense_hat import SenseHat
from labs.common.ActuatorData import ActuatorData
from labs.common.ConfigUtil import ConfigUtil
from labs.common.SensorData import SensorData
class SensorDataManager():
    actData=ActuatorData()
    nomTemp=0
    confP=ConfigUtil()
    '''
    this function takes sensorData as an argument and updates the ActuatorData object with the values and 
    returns the ActuatorData object.
    '''
    def handleSensorData(self,sensorData):        
            self.actData.setName(sensorData.getName())
            self.actData.setValue(sensorData.getCurrentValue())
            self.nomTemp=float(self.confP.getValue("device","nominalTemp"))
            if((self.nomTemp-5.0)<sensorData.getCurrentValue()<(self.nomTemp+5.0)):
                self.actData.setCommand("NEUTRAL")
            elif(sensorData.getCurrentValue()<(self.nomTemp+10.0)):
                self.actData.setCommand("TEMP DEC")
            elif(sensorData.getCurrentValue()>(self.nomTemp+10.0)):
                self.actData.setCommand("TEMP INC")   
           # print(self.actData.getCommand())             
            return self.actData    
    #return None
    def humidity(self,sensorData):
            self.actData.setName(sensorData.getName())
            self.actData.setValue(sensorData.getCurrentValue())
            self.actData.setCommand(str(round(sensorData.getCurrentValue(),2)))
            return self.actData
    def humidityI2C(self,sensorData):
            self.actData.setName(sensorData.getName())
            self.actData.setValue(sensorData.getCurrentValue())
            self.actData.setCommand(str(round(sensorData.getCurrentValue(),2)))
            return self.actData    