# goss-python
Python connector to goss. 

Requires Python 3.6 or above.

## Installation

- Clone repository
- Install into your python environment `pip install . `

## Creating a connection to GOSS

```` python

from goss import GOSS

def on_message_callback(header, message):
    print(f"header: {header} message: {message}")

# Note: there are other parameters for connecting to other
# systems than localhost
goss_client = GOSS(username="user", password="pass")

assert gapps.connected

goss_client.send('send.topic', {"foo": "bar"})

# Note we are sending the function not executing the function in the second parameter
goss_client.subscribe('subscrbe.topic', on_message_callback)

goss_client.send('subcribe.topic', 'A message about subscription')

time.sleep(5)

goss_client.close()

````


## Testing

The testing requires goss to be running in the docker container.  First install
the pytest environment `pip install pytest`.  Then run pytest from the root
of the goss-python environment. 
