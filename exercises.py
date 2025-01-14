#Read the json file and save the data
import json
with open('precipitation.json', 'r', encoding='utf-8') as file:
    precipitation_data = json.load(file)

#Read and save the stations
from csv import DictReader
with open('stations.csv') as file:
    stations = list(DictReader(file))

#Create output data structure
output_data = {}
for station in stations:
    output_data[station['Location']] = {
        'station': station['Station'],
        'state': station['State'],
        'total_monthly_precipitation': [0]*12,
        'total_yearly_precipitation': 0,
        'relative_monthly_precipitation': [0]*12,
        'relative_yearly_precipitation': 0
    }

#Create a dictionary that gets location based on station (to be used later)
station_to_location = {}
for item in stations:
    station_to_location[item['Station']] = item['Location']

#Calculate the total monthly and yearly percipitation for each location
#Also store the total percipitation (for all locations) for later use
total_percipitation = 0
for measurement in precipitation_data:
    #Calculate the index of the month by subtracting 1
    month_index = int(measurement['date'].split('-')[1]) - 1
    #Add the value to both the monthly and the yearly total
    location = station_to_location[measurement['station']]
    output_data[location]['total_monthly_precipitation'][month_index] += measurement['value']
    output_data[location]['total_yearly_precipitation'] += measurement['value']
    total_percipitation += measurement['value']
    
#Calculate relative monthly precipitation for each location for each month
#Calculate relative yearly precipitation for each location
for station in stations:
    #Calculate relative monthly precipitation
    location = station['Location']
    for month_index in range(0,12):
        #Define the relative monthly precipitation as a proportion of the monthly and yearly total
        output_data[location]['relative_monthly_precipitation'][month_index] = output_data[location]['total_monthly_precipitation'][month_index] / output_data[location]['total_yearly_precipitation']
    #Calculate relative yearly precipitation
    #Define relative yearly precipitation as a proportion of yearly total and total across all stations
    output_data[location]['relative_yearly_precipitation'] = output_data[location]['total_yearly_precipitation'] / total_percipitation
    
#Save the results to a json file
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file, indent=4)