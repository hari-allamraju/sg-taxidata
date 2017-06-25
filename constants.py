#File storage
TAXI_FILENAME='taxi.json'
TWO_HOUR_FILENAME='twohour.json'
HEAVY_RAIN_FILENAME='heavyrain.json'
PSI_FILENAME='psi.json'
TSTAMP='%Y-%m-%dT%H:%M:%S%z'
DATE='%Y%m%d'

#weather
TWO_HOUR="http://api.nea.gov.sg/api/WebAPI/?dataset=2hr_nowcast&keyref="
HEAVY_RAIN="http://api.nea.gov.sg/api/WebAPI/?dataset=heavy_rain_warning&keyref="
PSI="http://api.nea.gov.sg/api/WebAPI/?dataset=psi_update&keyref="

#SQL for the database
#taxi
TAXI_TABLE_CREATE_QUERY='create table if not exists taxis (id INTEGER primary key autoincrement,date TEXT, time TEXT,x INTEGER, y INTEGER,value INTEGER)'
TAXI_TABLE_INSERT_QUERY='insert into taxis (date,time,x,y,value) values (?,?,?,?,?)'
TAXI_BY_DATE_QUERY='select time,x,y,value from taxis where date=?'
TAXI_BY_DATE_AND_TIME_QUERY='select x,y,value from taxis where date=? and time=?'
TAXI_BY_TIME_QUERY='select date,x,y,value from taxis where time=?'
TAXI_BY_DATE_QUERY_XY='select time,x,y,value from taxis where date=? and x=? and y=?'
TAXI_BY_DATE_AND_TIME_QUERY_XY='select x,y,value from taxis where date=? and time=? and x=? and y=?'
TAXI_BY_TIME_QUERY_XY='select date,x,y,value from taxis where time=? and x=? and y=?'
#weather
TWO_HOUR_TABLE_CREATE_QUERY='create table if not exists twohour (id INTEGER primary key autoincrement,date TEXT, time TEXT,x INTEGER, y INTEGER,forecast TEXT,location TEXT)'
HEAVY_RAIN_TABLE_CREATE_QUERY='create table if not exists heavyrain (id INTEGER primary ket autoincrement,date TEXT, time TEXT, warning TEXT'
TWO_HOUR_TABLE_INSERT_QUERY='insert into twohour (date,time,x,y,forecast,location) values (?,?,?,?,?,?)'

#map details
#Singapore bounds as taken from Google maps - includes From Tuas to Changi and 
#from Sentosa to Woodlands
min_lat=1.237831
max_lat=1.470989
min_lon=103.605713
max_lon=104.043019
