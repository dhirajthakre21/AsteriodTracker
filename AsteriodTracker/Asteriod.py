#Tracking Asteroid 2020 LA by using NASA NeoWebService

#Importing Modules

import requests  
from pprint import pprint 
from datetime import datetime

date1=str(datetime.now())


api_key="qclKNF4Qk9pTsBDx6yTKR5jY5uOI6hVuPhhzd3hN"

#url
start_date=date1[:10]
end_date=date1[:8]+str(int(date1[8:10])+1)

url=  f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={api_key}'    

#getting data from URL
r=requests.get(url)
data=r.json()
list1=[]

data1=data['near_earth_objects']
all_data1=data1[start_date] 

'''for ast in all_data1 :
    if ast['name']=='163348 (2002 NN4)':
        break'''
#finding info by name :

for ast1 in all_data1 :
    list1.append(ast1['absolute_magnitude_h'])
    
for ast in all_data1 :
    if ast['absolute_magnitude_h']== min(list1):
    	break
    
print('Asteroid Name :' ,ast['name'])
print('Asteroid Id :' , ast['id'])
print('Asteroid NASA info :', ast['nasa_jpl_url'] ,)
print('absolute_magnitude' , ast['absolute_magnitude_h'])
print('Average Diameter :' ,ast['estimated_diameter']['meters']['estimated_diameter_max'])
print('Miss distance :' , ast['close_approach_data'][0]['miss_distance']['lunar'] ,'km')
print('Relative Velocity :', ast['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
print('orbiting body :' , ast['close_approach_data'][0]['orbiting_body'])
print('Is sentry object :' ,ast['is_sentry_object'])

    