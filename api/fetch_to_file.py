import json
from utils import create_data_folder,get_taxi_data
from constants import TAXI_FILENAME

path=create_data_folder()

taxi_file=path+"/"+TAXI_FILENAME

taxis=get_taxi_data()

with open(taxi_file,"w") as f:
	json.dump(taxis,f)