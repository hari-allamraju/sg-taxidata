import json
import requests
import datetime
import math
import os
import sqlite3
import datetime
from constants import *

def create_data_folder():
	now=datetime.datetime.now()
	tstamp=now.strftime(TSTAMP)
	path="data/"+now.strftime(DATE)+"/"+now.strftime('%H')+"{0:0>2}".format(int(5 * round(float(now.minute)/5)))

	if not os.path.exists(path):
		os.makedirs(path)

	return path

def get_taxi_data():
	#get and save data to file
	home = os.path.expanduser("~")
	key = open(home+"/keys/taxidataanalysis.key").read().strip()

	now=datetime.datetime.now()
	tstamp=now.strftime(TSTAMP)

	taxis = requests.get(
	    'https://api.data.gov.sg/v1/transport/taxi-availability',
	    params = {"date_time": tstamp},
	    headers = {"api-key": key}
	).json()
	return taxis

def read_json(filename):
	with open(filename,"r") as f:
		return json.loads(f.read())

def get_width(h):
	return int(h * (max_lon - min_lon) / (max_lat - min_lat))

def create_grid(h,value=0):
	w = get_width(h)
	grid = [[value] * (w+1) for i in range(h+1)]
	return grid

def get_grid_cell(lat,lon,h=20,w=None):
	w = get_width(h)
	cell_x = int((lon - min_lon) / (max_lon - min_lon) * w)
	cell_y = int((lat - min_lat) / (max_lat - min_lat) * h)
	return (cell_x,cell_y)

def get_rankings(grid):
	non_zero_cells = [
		item
		for row in grid
		for item in row if item != 0
	]

	sorted_cells = sorted(non_zero_cells)
	enumerated = enumerate(sorted_cells)
	rankings = {
		value: float(index)  / len(non_zero_cells)
		for (index, value) in enumerated
	}
	return rankings


def list_data_files(root,filename):
	result=[]
	for root, dirs, files in os.walk(root):
		if len(files) > 0 and filename in files:
			date,time = root.split("/")[1:]
			result.append((root+"/"+filename,date,time))
	return result

def process_data(directory,filename,f,grid_height=20):
	result=[]
	files = list_data_files(directory,filename)
	for file, date, time in files:
		grid=f(file,grid_height)
		result.append((date,time,grid))
	return result

def fetch_from_db(dbname,sql,params):
	result=[]
	db=sqlite3.connect(dbname)
	res=db.execute(sql,params)
	for r in res.fetchall():
		result.append(r)
	return result


