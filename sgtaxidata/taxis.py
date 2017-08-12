import sqlite3
from utils import *
from constants import *

def file_to_grid(filename,grid_height=20):
	grid=create_grid(grid_height)
	data=read_json(filename)
	for lon,lat in data['features'][0]['geometry']['coordinates']:
		x,y = get_grid_cell(lat,lon,grid_height)
		grid[y][x]+=1
	return grid

def load_taxi_to_db(dbname,directory,grid_height=20):
	db=sqlite3.connect(dbname)
	db.execute(TAXI_TABLE_CREATE_QUERY)
	data=process_data(directory,TAXI_FILENAME,file_to_grid,grid_height)
	grid_width=get_width(grid_height)
	for date, time, grid in data:
		for y in range(grid_height+1):
			for x in range(grid_width+1):
				db.execute(TAXI_TABLE_INSERT_QUERY,(date,time,x,y,grid[y][x]))
	db.commit()
	db.close()

def fetch_grid_by_date(dbname,date):
	return fetch_from_db(dbname,TAXI_BY_DATE_QUERY,(date,))

def fetch_grid_by_time(dbname,time):
	return fetch_from_db(dbname,TAXI_BY_TIME_QUERY,(time,))

def fetch_grid_by_date_and_time(dbname,date,time):
	return fetch_from_db(dbname,TAXI_BY_DATE_AND_TIME_QUERY,(date,time))

def fetch_loc_by_date(dbname,date,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_DATE_QUERY_XY,(date,x,y))

def fetch_loc_by_time(dbname,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_TIME_QUERY_XY,(time,x,y))

def fetch_loc_by_date_and_time(dbname,date,time,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,TAXI_BY_DATE_AND_TIME_QUERY_XY,(date,time,x,y))

def fetch_all_taxi_data_loc(dbname,lat,lon,grid_height=20):
	x,y=get_grid_cell(lat,lon,grid_height)
	return fetch_from_db(dbname,ALL_TAXI_BY_XY,(x,y))

def fetch_all_taxi_data(dbname):
	return fetch_from_db(dbname,ALL_TAXI,())

def getdf_loc_time(dbname,time,lat,lon):
    data=fetch_loc_by_time(dbname,time,lat,lon)
    df=getdf(data,['Date','X','Y','TaxiCount'],'Point')
    return df

def getdf_loc_date(dbname,date,lat,lon):
    data=fetch_loc_by_date(dbname,date,lat,lon)
    df=getdf(data,['Time','X','Y','TaxiCount'],'Point')
    return df

def getdf_date(dbname,date):
    data=fetch_grid_by_date(dbname,date)
    df=getdf(data,['Time','X','Y','TaxiCount'],'Point')
    return df

def getdf_loc_dates(dbname,dates,lat,lon):
    data=fetch_loc_by_date(dbname,dates[0],lat,lon)
    for date in dates[1:]:
    	data.extend(fetch_loc_by_date(dbname,date,lat,lon))
    df=getdf(data,['Time','X','Y','TaxiCount'],'Point')
    return df

def get_df_all_taxi_data_loc(dbname,lat,lon):
	data=fetch_all_taxi_data_loc(dbname,lat,lon)
	df=getdf(data,['Date','Time','X','Y','TaxiCount'],'Point')
	return df

def get_df_all_taxi_data(dbname):
	data=fetch_all_taxi_data(dbname)
	df=getdf(data,['Date','Time','X','Y','TaxiCount'],'Point')
	return df

def get_dates(dbname):
	dates=fetch_from_db(dbname,"select distinct date from taxis",())
	dates=[str(x[0]) for x in dates]
	return dates

