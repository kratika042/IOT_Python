from labs.common.ActuatorData import ActuatorData
import redis
import json
import math

class ActuatorDataListener():
    def onActuatorMessage(self, curVal):
        r=redis.Redis(host="localhost", port="6379")
        actData2=r.get("Actuator_Data").decode()
        curVal2=json.loads(actData2).get("currentVal")
       # print(curVal)
        #print(curVal2)
        if math.fabs(float(curVal)-float(curVal2))>5:
            print("Actuation took place..")
            print(actData2)
        else:
            print("No actuation")    
        
        return curVal2