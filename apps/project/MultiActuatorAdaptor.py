'''
Created on Feb 16, 2020

@author: Kratika Maheshwari
'''
from labs.module03.SenseHatLedActivator import SenseHatLedActivator
class MultiActuatorAdaptor():
    shla=SenseHatLedActivator()
    '''
    function updateActuator takes object of class ActuatorData as an argument, it is called to display the output to sense hat
    by calling the function show()
    '''
    def updateActuator(self,ActuatorData):
            try:
                self.shla.show(ActuatorData.getCommand())
                return True
            except:
                return False