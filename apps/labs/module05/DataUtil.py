'''
Created on Feb 22, 2020

@author: Kratika Maheshwari
'''
import json
class DataUtil:
    
    def __init__(self):
        pass
    def toJsonFromSensorData(self,sensorData):
        data={}
        data["name"]=sensorData.getName();
        data["timestamp"]=sensorData.getTimestamp();
        data["currentValue"]=sensorData.getCurrentValue();
        data["averageValue"]=sensorData.getAverageValue();
        data["minValue"]=sensorData.getMinValue();
        data["maxValue"]=sensorData.getMaxValue();
        data["count"]=sensorData.getCount();
       # j=json.dumps(self.data)
        j=json.dumps(data)
        return j
    def toActuatorDataFromJson(self, json1):
        j=json1.replace("{","").replace("}","");
       # return (j[2].split(":")[1])
        return j
    def toSensorDataFromJson(self,json2):
        j=json2.replace("{","").replace("}","").split(",");
        
        return (j[2].split(":")[1])    