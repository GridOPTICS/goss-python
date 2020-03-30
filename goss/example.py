from goss import GOSS

import time

client = GOSS(stomp_address='localhost', stomp_port='61613')

def on_message_callback(header, message):
    print(f"header: {header} message: {message}")
    
    
client.subscribe('/topic/goss.example.1234', on_message_callback)


client.send('/topic/goss.example.1234', 'this is a test message')

time.sleep(5)

client.close()
