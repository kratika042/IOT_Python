'''
Created on Jan 26, 2020

@author: Kratika Maheshwari
'''
import configparser;
from os import path
confP=configparser.ConfigParser()

class ConfigUtil:
    
    '''
    filepath is set and loadConfig method is called.
    '''
    def __init__(self):
        self.filepath='../../config/ConnectedDevicesConfig.props';
        self.dictSMTP={}
        self.loadConfig(self.filepath)
        
    '''
    This function checks for the existence of the file.
    '''    
    def hasConfig(self):
        if(path.exists(self.filepath)):
            return True
        return False
    
    '''
    This function loads the value of all the required variables of config file and store in a dictionary.
    '''
    def loadConfig(self,filepath):
        if(self.hasConfig()):
            confP.read(self.filepath)
            self.dictSMTP['hostName']=self.getValue("smtp.cloud", "host")
            self.dictSMTP['portNumber']=self.getValue("smtp.cloud", "port")
            self.dictSMTP['token']=self.getValue('smtp.cloud','authToken')
            self.dictSMTP['senderAddr']=self.getValue("smtp.cloud", "fromAddr")
            self.dictSMTP['receiverAddr']=self.getValue("smtp.cloud", "toAddr")
            return True
        else:
            print("File doesn't exist")
            return False
        
    '''
    This function returns the value associated with the key.
    '''    
    def getValue(self,section,key):
        return confP.get(section,key)
    
    '''
    getter function for the dictionary.
    '''
    def dictSmtp(self):
        return self.dictSMTP
    