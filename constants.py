#File storage
FILENAME='data.json'
TSTAMP='%Y-%m-%dT%H:%M:%S%z'
DATE='%Y%m%d'


#SQL for the database
TABLE_CREATE_QUERY='create table if not exists taxis (id INTEGER primary key autoincrement,date TEXT, time TEXT,x INTEGER, y INTEGER,value INTEGER)'
TABLE_INSERT_QUERY='insert into taxis (date,time,x,y,value) values (?,?,?,?,?)'
BY_DATE_QUERY='select time,x,y,value from taxis where date=?'
BY_DATE_AND_TIME_QUERY='select x,y,value from taxis where date=? and time=?'
BY_TIME_QUERY='select date,x,y,value from taxis where time=?'


#map details
#Singapore bounds as taken from Google maps - includes From Tuas to Changi and 
#from Sentosa to Woodlands
min_lat=1.237831
max_lat=1.470989
min_lon=103.605713
max_lon=104.043019
