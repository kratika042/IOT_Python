import unittest


"""
Test class for all requisite Module04 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.common.ConfigUtil import ConfigUtil
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData
from labs.module03.SensorDataManager import SensorDataManager
from labs.module04.MultiActuatorAdaptor import MultiActuatorAdaptor
class Module04Test(unittest.TestCase):

	confU=ConfigUtil();
	sensorD=SensorData()
	hasConf=confU.hasConfig()
	curVal=sensorD.getCurrentValue()
	avgVal=sensorD.getAverageValue()
	actD=ActuatorData()
	senDM=SensorDataManager()
	multiAct=MultiActuatorAdaptor()
	"""
	it checks for the datatype of hasConf to be boolean, If true test case is passed.
	"""

	def testConfigUtil(self):
		self.assertTrue(isinstance(self.hasConf,bool),"Boolean Value")
		
	"""
	it checks for the datatype of curVal to be float, If true test case is passed. 
	Second checks for the avgVal to be within the specified range.If true test case is passed. 
	"""	
	def testSensorData(self):
		self.assertTrue(isinstance(self.curVal,float),"Float Value")
		self.assertTrue(self.avgVal>=0.0 and self.avgVal<=30.0,"Average Temperature within the range")
	'''
	It checks for the datatype of the getCommand function to be String.
	'''	
	def testActuatorData(self):
		self.assertTrue(isinstance(self.actD.getCommand(),str), "String")
		
	'''
	It checks for the returntype of the function handleSensorData of class SensorDataManager to be of type actuator data. 
	'''	
	def testSensorDataManager(self):
		self.assertTrue(isinstance(self.senDM.handleSensorData(self.sensorD),ActuatorData), "Type Actuator Data")		
	'''
	It checks for the returntype of the function updateActuator of class MultiActuatorAdaptor to be of type Boolean. 
	'''	
	def testMultiActuatorAdaptor(self):
		self.assertTrue(isinstance(self.multiAct.updateActuator(ActuatorData),bool), "Type Boolean")		
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()