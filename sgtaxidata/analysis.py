import taxis
from datetime import datetime
import geocoder

def get_lat_long(location):
    g=geocoder.google(location)
    if g.response.status_code == 200:
        c=g.geojson['features'][0]['geometry']['coordinates']
        return (c[1],c[0])

def peak(h,m,w):
    return 1 if ((w==1 and (h>=6 and (h <=9 and m<30)) or (h >= 18))) else 0

def weekday(d):
    dt=datetime.strptime(d,"%Y%m%d")
    return 1 if datetime.isoweekday(dt)<6 else 0

def get_weekday_data(date,dbname,lat,lon,high=0.9,low=0.1,holidays=[]):
    if weekday(date)==0:
        return None
    df=taxis.getdf_loc_date(dbname,date,lat,lon)
    h=df.quantile(q=high)['TaxiCount']
    l=df.quantile(q=low)['TaxiCount']
    df['Date']=date
    df['Hour']=df.apply(lambda r:int(r['Time'][:2]),axis=1)
    df['Minute']=df.apply(lambda r:int(r['Time'][2:]),axis=1)
    df['Weekday']=df.apply(lambda r: weekday(r['Date']),axis=1)
    df['Holiday']=df.apply(lambda r: 1 if r['Date'] in holidays else 0,axis=1)
    df['PeakHour']=df.apply(lambda r: peak(r['Hour'],r['Minute'],r['Weekday']),axis=1)
    df=df.query('(TaxiCount>=@l and TaxiCount<=@h) and Weekday==1')[['Hour','Minute','PeakHour','TaxiCount']]
    return df

