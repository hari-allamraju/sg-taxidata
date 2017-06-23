import requests
import math
import os
import json
from constants import *
from utils import create_data_folder
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring


#get and save data to file
home = os.path.expanduser("~")
key = open(home+"/keys/neaweather.key").read().strip()

path=create_data_folder()

two_hour_file=path+"/"+TWO_HOUR_FILENAME
heavy_rain_file=path+"/"+HEAVY_RAIN_FILENAME
psi_file=path+"/"+PSI_FILENAME

two_hour = requests.get(TWO_HOUR+key).text
heavy_rain = requests.get(HEAVY_RAIN+key).text
psi_update = requests.get(PSI+key).text

with open(two_hour_file,"w") as f:
	json.dump(bf.data(fromstring(two_hour)),f)

with open(heavy_rain_file,"w") as f:
	json.dump(bf.data(fromstring(heavy_rain)),f)

with open(psi_file,"w") as f:
	json.dump(bf.data(fromstring(psi_update)),f)
