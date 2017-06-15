import json
import os
from constants import *

def read_json(filename):
	with open(filename,"r") as f:
		return json.loads(f.read())

def get_width(h):
	return int(h * (max_lon - min_lon) / (max_lat - min_lat))

def create_grid(h,w):
	grid = [[0] * (h+1) for i in range(w+1)]
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

def list_data_files(root):
	result=[]
	for root, dirs, files in os.walk(root):
		if len(files) > 0 and FILENAME in files:
			date,time = root.split("/")[1:]
			result.append((root+"/"+FILENAME,date,time))
	return result
