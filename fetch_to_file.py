import requests
import datetime
import math
import os
import json
from constants import *

#get and save data to file
home = os.path.expanduser("~")
key = open(home+"/keys/taxidataanalysis.key").read().strip()

now=datetime.datetime.now()
tstamp=now.strftime(TSTAMP)
path="data/"+now.strftime(DATE)+"/"+now.strftime('%H')+str(int(5 * round(float(now.minute)/5)))

if not os.path.exists(path):
    os.makedirs(path)

filename=path+"/"+FILENAME

taxis = requests.get(
    'https://api.data.gov.sg/v1/transport/taxi-availability',
    params = {"date_time": tstamp},
    headers = {"api-key": key}
).json()

with open(filename,"w") as f:
	json.dump(taxis,f)