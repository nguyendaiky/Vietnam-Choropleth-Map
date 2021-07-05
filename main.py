import json
import pandas as pd 

vietnam = json.load(open('diaphantinh.geojson','r'))
df = pd.read_csv('mat-do-dan-so.csv')

id_map = {}
for feature in vietnam['features']:
    feature['id'] = feature['properties']['code']
    id_map[feature['properties']['ten_tinh']] = feature['id']
print(id_map)