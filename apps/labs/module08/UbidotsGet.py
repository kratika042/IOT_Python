'''
Created on Apr 14, 2020

@author: Kratika Maheshwari
'''
import json
import requests

token = "BBFF-08hJyBD6jtjlrxddzfS6pmyGfgMgX8"

"""
Get values from variable 
"""
def get_values(device_label, var_label, items):

    base_url = "http://things.ubidots.com/api/v1.6/devices/" + device_label + "/" + var_label + "/values"
    try:
        r = requests.get(base_url + '?token=' + token + "&page_size=" + str(items), timeout=20)
        return r.json()
    except Exception as e:
        print(e)
        return {'error':'Request failed or timed out'}

"""
Main function
"""
if __name__ == '__main__':
    
    device_label = "temperature-sensor"
    var_label1 = "currenttemp"
    var_label2="averagetemp"

    print("Current Temperature Values")
    values = get_values(device_label, var_label1, 20)
    for i in values['results']:
        print(i)
    print("**********") 
    print("Average Temperature Values")   
    values=get_values(device_label, var_label2, 20)
    for i in values['results']:
        print(i)    