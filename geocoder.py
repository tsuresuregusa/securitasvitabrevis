#!/usr/bin/env python3
import pandas as pd
from geopy.geocoders import Bing

bing_key = 'ginITT5ALcrOnA4aMoH0~_vGQBu-_tnKr6FYRj6U5nA~Ar9conblprRVoeaB4uH4PKMzcs0BfrUJ5LbspSyDn04UqCpCOfsm567DJjUw-PY6'

def get_geocode(row):
    geolocator = Bing(bing_key, timeout=7)
    location = geolocator.geocode(row)
    if location is None:
    	print("NOT FOUND")
    	return "NOT FOUND"
    else:
    	if location.raw["address"]["countryRegion"] == "Chile":
    		r = str(location.latitude) + ", " + str(location.longitude)
    		print(r)
    		return r
    	else:
    		print("MISFORMED")
    		return "MISFORMED"


def parsingData(pathToCSV):
	data = pd.read_csv(pathToCSV,sep=',')
	# Geocoding #
	data['Coordenadas'] = (data['KAKA'] + ", ñuñoa, santiago, Chile").apply(get_geocode)
	# Lat and Lon
	lat = lambda row: row.split(',')[0].strip()
	lon = lambda row: row.split(',')[-1].strip()
	data['lat'] = data['Coordenadas'].map(lat)
	data['lon'] = data['Coordenadas'].map(lon)
	data.drop(labels=['Coordenadas'],axis=1,inplace=True)
	# Saving to CSV
	name = pathToCSV.split('.')[0] + '_coorLatLon.' + pathToCSV.split('.')[1]
	data.to_csv(name,sep=',')

pathToCSV = '~/Documents/fiscalia_julio.csv'
data = pd.read_csv(pathToCSV,sep=',')
#print(data['KAKA'])
data['KAKA2'] = data['KAKA'] + ", ñuñoa, santiago, Chile"
print(data['KAKA2'])
parsingData(pathToCSV)
