'''
Created on Feb 22, 2020

@author: Kratika Maheshwari
'''
import redis
cl=redis.Redis(host="localhost",port="6379")
cl.set("name","hello")
print(cl.get("name"))