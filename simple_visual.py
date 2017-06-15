import colorsys
import sys
from utils import *

#colors
W = '\033[0m'  # white (normal)
R = '\033[31m' # red
G = '\033[32m' # green
O = '\033[33m' # orange
B = '\033[34m' # blue
P = '\033[35m' # purple

	
def display_grid(grid):
	rankings=get_rankings(grid)
	for row in reversed(grid):
		strs = []
		for n in row:
			if n == 0:
				strs.append("   ")
			else:

				(r, g, b) = colorsys.hsv_to_rgb(1-rankings[n], 1, 1)
				
				def scale(float_zero_to_one):
					return min(5, int(6 * float_zero_to_one))
					 
				color_index = 16 + 36 * scale(r) + 6 * scale(g) + scale(b)  
				color = "\033[38;5;" + str(color_index) + "m"
				
				strs.append(color + str(n).rjust(3, " ") + W)
		print("".join(strs))


if __name__=="__main__":
	if len(sys.argv) < 2:
		print "Usage: python simple_visual.py <data file name>"
		sys.exit(1)
	h=20
	w=get_width(h)
	grid=create_grid(w,h)
	data=read_json(sys.argv[1])
	points=data['features'][0]['geometry']['coordinates']
	for lon,lat in points:
		x,y=get_grid_cell(lat,lon,w,h)
		grid[y][x]+=1
	display_grid(grid)

