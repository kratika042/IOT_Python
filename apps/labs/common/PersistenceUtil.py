'''
Created on Feb 22, 2020

@author: Kratika Maheshwari
'''
import json
import redis
from labs.module05.DataUtil import DataUtil
from distutils import command
class PersistenceUtil:
    
    def __init__(self):
        pass
    def writeSensorDataToDbms(self,sd):
        du=DataUtil()
        d=du.toJsonFromSensorData(sd)
        data=json.loads(d)
     #   print(data)
        c=redis.Redis(host="localhost",port="6379")
        c.set(sd.getName(),str(data))
        
    def getSensorDataFromDbms(self):
        r=redis.Redis(host="localhost", port="6379")
        actData2=r.get("Temperature")
        if(actData2==None):
            return  None
        else:
            actData2=actData2.decode()
            du=DataUtil()
            curVal=du.toSensorDataFromJson(actData2)
            return curVal
        
    def getActuatorDataFromDbms(self):
        r=redis.Redis(host="localhost", port="6379")
        actData2=r.get("Actuator_Data")
        if(actData2==None):
            return "1"
        else:
            actData2=actData2.decode()
            du=DataUtil()
         #   curVal=du.toActuatorDataFromJson(actData2)
          #  return curVal
            j=du.toActuatorDataFromJson(actData2)
            return j
    def writeActuatorDataToDbms(self):
      #  print("inside pu")
        r=redis.Redis(host="localhost", port="6379")
        sData=r.get("Temperature")
        if(sData==None):
            return "3"
        sData=sData.decode()
        j=sData.replace("{","").replace("}","").split(",");
        data={}
        data["command"]="TEMP INC"
        data["name"]=j[0].split(":")[1]
        data["currentVal"]=j[2].split(":")[1];
        data=json.dumps(data)
        print(data)
        r.set("Actuator_Data",str(data))
        