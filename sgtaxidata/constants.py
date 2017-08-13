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
TAXI_RAW_TABLE_CREATE_QUERY='create table if not exists taxis_raw (id INTEGER primary key autoincrement,date TEXT, time TEXT,lat REAL, lon REAL)'
TAXI_TABLE_INSERT_QUERY='insert into taxis (date,time,x,y,value) values (?,?,?,?,?)'
TAXI_RAW_TABLE_INSERT_QUERY='insert into taxis_raw (date,time,lat,lon) values (?,?,?,?)'
TAXI_BY_DATE_QUERY='select time,x,y,value from taxis where date=?'
TAXI_BY_DATE_AND_TIME_QUERY='select x,y,value from taxis where date=? and time=?'
TAXI_BY_TIME_QUERY='select date,x,y,value from taxis where time=?'
TAXI_BY_DATE_QUERY_XY='select time,x,y,value from taxis where date=? and x=? and y=?'
TAXI_BY_DATE_AND_TIME_QUERY_XY='select x,y,value from taxis where date=? and time=? and x=? and y=?'
TAXI_BY_TIME_QUERY_XY='select date,x,y,value from taxis where time=? and x=? and y=?'
ALL_TAXI_BY_XY='select date,time,x,y,value from taxis where x=? and y=?'
ALL_TAXI='select date,time,x,y,value from taxis'
ALL_TAXI_RAW='select date,time,lat,lon from taxis_raw'
#weather
TWO_HOUR_TABLE_CREATE_QUERY='create table if not exists twohour (id INTEGER primary key autoincrement,date TEXT, time TEXT,x INTEGER, y INTEGER,forecast TEXT,location TEXT)'
HEAVY_RAIN_TABLE_CREATE_QUERY='create table if not exists heavyrain (id INTEGER primary ket autoincrement,date TEXT, time TEXT, warning TEXT'
TWO_HOUR_TABLE_INSERT_QUERY='insert into twohour (date,time,x,y,forecast,location) values (?,?,?,?,?,?)'
TWO_HOUR_BY_DATE_QUERY='select time,x,y,forecast,location from twohour where date=?'
TWO_HOUR_BY_DATE_AND_TIME_QUERY='select x,y,forecast,location from twohour where date=? and time=?'
TWO_HOUR_BY_TIME_QUERY='select date,x,y,forecast,location from twohour where time=?'
TWO_HOUR_BY_DATE_QUERY_XY='select time,x,y,forecast,location from twohour where date=? and x between ? and ? and y between ? and ?'
TWO_HOUR_BY_DATE_AND_TIME_QUERY_XY='select x,y,forecast,location from twohour where date=? and time=? and x between ? and ? and y between ? and ?'
TWO_HOUR_BY_TIME_QUERY_XY='select date,x,y,forecast,location from twohour where time=? and x between ? and ? and y between ? and ?'

WEATHER_CODES={}
#bad
for i in ['BR','CL','DR','FG','HG','HR','HS','HT','HZ','LH ','LR','LS']:
	WEATHER_CODES[i]=0
#good
for i in ['FA','FN','FW','SU']:
	WEATHER_CODES[i]=1
#moderate
for i in ['OC','PC','PN','PS','RA','SH','SK','SN','SR','SS','SW','TL','WC','WD','WF','WR','WS']:
	WEATHER_CODES[i]=0.5

#map details
#Singapore bounds as taken from Google maps - includes From Tuas to Changi and 
#from Sentosa to Woodlands
min_lat=1.237831
max_lat=1.470989
min_lon=103.605713
max_lon=104.043019
