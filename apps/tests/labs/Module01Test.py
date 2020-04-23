import unittest


from labs.module01.SystemCpuUtilTask import SystemCpuUtilTask
from labs.module01.SystemMemUtilTask import SystemMemUtilTask

'''This is testing module having 2 functions which will test the cases for CPU and Memory Utilization outputs.'''

class Module01Test(unittest.TestCase):
	cpuUtil=SystemCpuUtilTask()
	
	'''
	 This function tests the outcomes of Memory Utilization.
	 1. Case 1 is that it will check for the output to be of data type float.
	 2. Case 2 is that it will check for the output should be within the range 0.0 to 100.0
	 test case will pass if the condition is true.
	'''
	
	
	def testMemUtil(self):
		memUtil=SystemMemUtilTask();
		self.assertTrue(isinstance(memUtil.getDataFromSensor(),float),"Float Value")
		self.assertTrue(memUtil.getDataFromSensor()>=0.0 and memUtil.getDataFromSensor()<=100.0,"in range")
	
	"""
	This function tests the outcomes of CPU Utilization.
	1. Case 1 is that it will check for the output to be of data type float.
	2. Case 2 is that it will check for the output should be within the range 0.0 to 100.0
	test case will pass if the condition is true.
	"""
	def testCpuUtil(self):
		cpuUtil=SystemCpuUtilTask();
		self.assertTrue(isinstance(cpuUtil.getDataFromSensor(),float),"Float value")
		self.assertTrue(cpuUtil.getDataFromSensor()>=0.0 and cpuUtil.getDataFromSensor()<=100.0,"in range")

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()