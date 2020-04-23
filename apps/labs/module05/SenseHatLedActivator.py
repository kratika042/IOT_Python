'''
Created on Feb 7, 2020

@author: Kratika Maheshwari
'''
from sense_hat import SenseHat

class SenseHatLedActivator():
    '''
    sense hat object is created.
    '''
    sense=SenseHat()
    
    '''
    inside show function command of actuator data is sent as a parameter
    '''
    def show(self,command):
        #print("here!!!!")
        if(command=="TEMP INC"):            #condition is checked for temperature increased
            msg="I"                           #msg is set to "I" to display in sense Hat
        elif(command=="TEMP DEC"):          #condition is checked for temperature decreased
            msg="D"                         #msg is set to "D" to display in sense Hat
        elif(command=="NEUTRAL"):                               #neutral condition 
            msg="N"    
        else:
            msg=command                         #msg is set to "N" to display in sense Hat
        self.sense.show_message(msg)        #calling of show_message function of sense hat.
    