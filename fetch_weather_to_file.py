import requests
import math
import os
import json
from constants import *
from utils import create_data_folder


#get and save data to file
home = os.path.expanduser("~")
key = open(home+"/keys/neaweather.key").read().strip()

path=create_data_folder()

two_hour_file=path+"/"+TWO_HOUR_FILENAME
heavy_rain_file=path+"/"+HEAVY_RAIN_FILENAME
psi_file=path+"/"+PSI_FILENAME
