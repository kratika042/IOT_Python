'''
Created on Jan 26, 2020

@author: Kratika Maheshwari
'''
import smtplib
from labs.common.ConfigUtil import ConfigUtil
class SmtpClientConnector:
    
    '''
    This function is called if the trigger value reaches, all the required values for connection
     are fetched from ConfigUtil class, and email format is created and sent to the receiver.
    '''
    def connector(self,command):
        confUtil=ConfigUtil()
        if(command=="TEMP INC"):
            
            msg="Current temperature value exceeds the nominal temperature value."
        elif(command=="TEMP DEC"):
            msg="Current temperature value deceeds the nominal temperature value."   
        else:
            msg="Current temperature value neutral to the nominal temperature value."     
        sub="Temperature Alert"
        message='Subject: {}\n\n{}'.format(sub,msg)
        dictS=confUtil.dictSmtp()
        senderAddr=dictS['senderAddr']
        receiverAddr=dictS['receiverAddr']
        hostName=dictS['hostName']
        portNumber=dictS['portNumber']
        token=dictS['token']
        server=smtplib.SMTP(hostName,portNumber)
        server.starttls()
        server.login(senderAddr,token)
        server.ehlo()
        server.sendmail(senderAddr, receiverAddr, message)       