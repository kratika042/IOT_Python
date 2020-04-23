'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
from labs.common.ActuatorData import ActuatorData
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
class TempActuatorAdaptor():
    command=""
    tempValue=0.0
    '''
    object of SenseHatLedActivator class is created
    '''
    shla=SenseHatLedActivator()
    '''
    function updateActuator takes object of class ActuatorData as an argument, it is called to display the output to sense hat
    by calling the fucntion show()
    '''
    def updateActuator(self,ActuatorData):
       
            self.shla.show(ActuatorData.getCommand())
            
              
        
        