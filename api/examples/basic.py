import requests
import time
from os.path import expanduser


#just get and print data to prove that the API key works
home = expanduser("~")
key = open(home+"/keys/taxidataanalysis.key").read().strip()

tstamp=time.strftime('%Y-%m-%dT%H:%M:%S%z')

taxis = requests.get(
    'https://api.data.gov.sg/v1/transport/taxi-availability',
    params = {"date_time": tstamp},
    headers = {"api-key": key}
).json()

print taxis