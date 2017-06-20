import json
import os
import sqlite3
from constants import *

def read_json(filename):
	with open(filename,"r") as f:
		return json.loads(f.read())

def get_width(h):
	return int(h * (max_lon - min_lon) / (max_lat - min_lat))

def create_grid(w,h):
	grid = [[0] * (w+1) for i in range(h+1)]
	return grid

def get_grid_cell(lat,lon,w,h):
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

def file_to_grid(filename,grid_height=20):
	grid_width=get_width(grid_height)
	grid=create_grid(grid_width,grid_height)
	data=read_json(filename)
	for lon,lat in data['features'][0]['geometry']['coordinates']:
		x,y = get_grid_cell(lat,lon,grid_width,grid_height)
		grid[y][x]+=1
	return grid


def list_data_files(root):
	result=[]
	for root, dirs, files in os.walk(root):
		if len(files) > 0 and FILENAME in files:
			date,time = root.split("/")[1:]
			result.append((root+"/"+FILENAME,date,time))
	return result

def process_data(directory,grid_height=20):
	result=[]
	files = list_data_files(directory)
	for filename, date, time in files:
		grid=file_to_grid(filename,grid_height)
		result.append((date,time,grid))
	return result

def load_to_db(dbname,directory,grid_height=20):
	db=sqlite3.connect(dbname)
	db.execute(TABLE_CREATE_QUERY)
	data=process_data(directory,grid_height)
	grid_width=get_width(grid_height)
	for date, time, grid in data:
		for i in range(grid_height+1):
			for j in range(grid_width+1):
				db.execute(TABLE_INSERT_QUERY,(date,time,i,j,grid[i][j]))
	db.commit()
	db.close()

def fetch_from_db(dbname,sql,params):
	result=[]
	db=sqlite3.connect(dbname)
	res=db.execute(sql,params)
	for r in res.fetchall():
		result.append(r)
	return result

def fetch_by_date(dbname,date):
	return fetch_from_db(dbname,BY_DATE_QUERY,(date,))

def fetch_by_time(dbname,time):
	return fetch_from_db(dbname,BY_TIME_QUERY,(time,))

def fetch_by_date_and_time(dbname,date,time):
	return fetch_from_db(dbname,BY_DATE_AND_TIME_QUERY,(date,time))



