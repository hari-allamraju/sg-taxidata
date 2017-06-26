import sqlite3
from utils import *
from constants import *


def file_to_grid(filename,grid_height=20):
	grid=create_grid(grid_height,('-','-'))
	data=read_json(filename)
	for d in data['channel']['item']['weatherForecast']['area']:
		lat=d['@lat']
		lon=d['@lon']
		forecast=d['@forecast']
		location=d['@name']
		x,y = get_grid_cell(lat,lon,grid_height)
		grid[y][x]=(forecast,location)
	return grid


def load_two_hour_to_db(dbname,directory,grid_height=20):
	db=sqlite3.connect(dbname)
	db.execute(TWO_HOUR_TABLE_CREATE_QUERY)
	data=process_data(directory,TWO_HOUR_FILENAME,file_to_grid,grid_height)
	grid_width=get_width(grid_height)
	for date, time, grid in data:
		for y in range(grid_height+1):
			for x in range(grid_width+1):
				forecast,location=grid[y][x]
				if not forecast=='-':
					db.execute(TWO_HOUR_TABLE_INSERT_QUERY,(date,time,x,y,forecast,location))
	db.commit()
	db.close()

def fetch_grid_by_date(dbname,date):
	return fetch_from_db(dbname,TWO_HOUR_BY_DATE_QUERY,(date,))

def fetch_grid_by_time(dbname,time):
	return fetch_from_db(dbname,TWo_HOUR_BY_TIME_QUERY,(time,))

def fetch_grid_by_date_and_time(dbname,date,time):
	return fetch_from_db(dbname,TWO_HOUR_BY_DATE_AND_TIME_QUERY,(date,time))

def fetch_loc_by_date(dbname,date,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TWO_HOUR_BY_DATE_QUERY_XY,(date,x,y))

def fetch_loc_by_time(dbname,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TWO_HOUR_BY_TIME_QUERY_XY,(time,x,y))

def fetch_loc_by_date_and_time(dbname,date,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TWO_HOUR_BY_DATE_AND_TIME_QUERY_XY,(date,time,x,y))

