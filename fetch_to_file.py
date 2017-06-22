import requests
import datetime
import math
import os
import json
from constants import *
from utils import create_data_folder

#get and save data to file
home = os.path.expanduser("~")
key = open(home+"/keys/taxidataanalysis.key").read().strip()

path=create_data_folder()

taxi_file=path+"/"+TAXI_FILENAME

now=datetime.datetime.now()
tstamp=now.strftime(TSTAMP)

taxis = requests.get(
    'https://api.data.gov.sg/v1/transport/taxi-availability',
    params = {"date_time": tstamp},
    headers = {"api-key": key}
).json()

with open(taxi_file,"w") as f:
	json.dump(taxis,f)