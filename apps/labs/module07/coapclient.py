from coapthon.client.helperclient import HelperClient
from labs.module05.DataUtil import DataUtil

import json
from coapthon.client import coap
from labs.module07.exampleresources import BasicResource
from labs.common.SensorData import SensorData
from test.support import join_thread
class coapclient:
    host = "127.0.0.1"
    port = 5683
    path ="coap://127.0.0.1:5683"
    du=DataUtil()
    def coapTest(self, s):
       # print("here")
        client = HelperClient(server=(self.host, self.port))
      #  print(s)
        join_thread
        client.get(self.path)
        #client.post(path, "1")
        
       # json2=json.loads(s)
      #  print("hello")
        
        client.put(self.path,payload=self.du.toSensorDataFromJson(s))
        BasicResource()
        #client.get(path)
        client.delete(self.path, timeout=2)
        #client.get(path)
    #    client.post(self.path,payload=self.du.toSensorDataFromJson(s))
        #client.get(path)
        #client.put(path,payload="2")
        
        
        client.stop()