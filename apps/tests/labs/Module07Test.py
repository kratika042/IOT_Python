import unittest


"""
Test class for all requisite Module07 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData
from labs.module05.DataUtil import DataUtil
from labs.module05.ActuatorDataListener import ActuatorDataListener
import json
class Module07Test(unittest.TestCase):
	sensorD=SensorData()
	#hasConf=confU.hasConfig()
	curVal=sensorD.getCurrentValue()
	avgVal=sensorD.getAverageValue()
	actD=ActuatorData()
	du=DataUtil()
	adl=ActuatorDataListener()
	j="";

	def testSensorData(self):
		self.assertTrue(isinstance(self.curVal,float),"Float Value")
		self.assertTrue(self.avgVal>=0.0 and self.avgVal<=30.0,"Average Temperature within the range")
	'''
	It checks for the datatype of the getCommand function to be String.
	'''	
	def testDataUtil(self):
		self.assertTrue(isinstance(self.du.toJsonFromSensorData(self.sensorD),str), "String")
		
	def testActuatorDataFromJson(self):
		self.assertTrue(isinstance(self.du.toActuatorDataFromJson(self.j),str), "String")
	def testActuatorDataListener(self):
		self.assertTrue(isinstance(self.adl.onActuatorMessage(str(self.curVal)),float), "Type String")
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()