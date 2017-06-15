import json

#Singapore bounds as taken from Google maps - includes From Tuas to Changi and 
#from Sentosa to Woodlands
min_lat=1.237831
max_lat=1.470989
min_lon=103.605713
max_lon=104.043019

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
