'''
Created on Sep 9, 2019

@author: shar064
'''

from goss import GOSS,utils
import time

def on_message_callback(header, message):
    print(message)

if __name__ == '__main__':
    
    goss_client = GOSS(username=utils.get_goss_user(),password=utils.get_goss_pass())
    assert goss_client.connected
    goss_client.subscribe("goss.test", on_message_callback)
    goss_client.send("goss.test", "This is a test message")
   
    time.sleep(5)
    
        
    