import unittest
from labs.common.ConfigUtil import ConfigUtil
from labs.common.SensorData import SensorData
from labs.module02.TempSensorEmulatorTask import TempSensorEmulatorTask
class Module02Test(unittest.TestCase):
	"""
	class scoped variables and objects are created
	"""
	confU=ConfigUtil();
	sensorD=SensorData()
	tempSensor=TempSensorEmulatorTask()
	curVal=0.0
	avgVal=0.0
	hasConf=""
	data=None;
	
	'''
	values are setup into the variables
	 '''
	def setUp(self):
		self.data=self.tempSensor.getSensorData()
		self.hasConf=self.confU.hasConfig()
		self.curVal=self.sensorD.getCurrentValue()
		self.avgVal=self.sensorD.getAverageValue()
		

	"""
	All the resources are tear down here.
	"""
	def tearDown(self):
		del self.data
		del self.hasConf
		del self.curVal
		del self.avgVal
	
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
	It checks for the datatype of data to be of class type SensorData, If true test case is passed.
	'''	
	def testTemperatureSensorEmulatorTask(self):
		self.assertTrue(isinstance(self.data,SensorData),"Sensor Data Type Value")
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()