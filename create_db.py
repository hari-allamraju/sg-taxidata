import sys

from utils import *

if __name__=="__main__":
	if len(sys.argv) < 4:
		print "Usage: python simple_visual.py <data directory> <db name> <grid height>"
		sys.exit(1)
	directory=sys.argv[1]
	dbname=sys.argv[2]
	height=int(sys.argv[3])

	load_to_db(dbname,directory,height)