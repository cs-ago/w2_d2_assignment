#EXERCISE 1
#EXERCISES 1.1: Read the json file and save the data
import json
with open('precipitation.json', 'r', encoding='utf-8') as file:
    precipitation_data = json.load(file)

#EXERCISE 1.2 and 1.3: Calculate the monthly total precipitation for Seattle
seattle_data = []
for measurement in precipitation_data:
    if measurement['station'] == 'GHCND:US1WAKG0038':
        seattle_data.append(measurement)

#EXERCISE 1.3: TOTAL MONTHLY PERCIPITATION FOR SEATTLE
#Crate a list of 12 zeros for the months
seattle_total_monthly_precipitation = [0]*12
#EXERCISE 2.1: CALCUATE THE TOTAL YEARLY PERCIPITATION
seattle_total_yearly_precipitation = 0
for measurement in seattle_data:
    #Calculate the index of the month by subtracting 1
    month_index = int(measurement['date'].split('-')[1]) - 1
    #Add the value to both the monthly and the yearly total
    seattle_total_monthly_precipitation[month_index] += measurement['value']
    seattle_total_yearly_precipitation += measurement['value']
    
#EXERCISE 2.2: CALCULATE RELATIVE MONTHLY PERCIPITATION
seattle_relative_monthly_precipitation = [0]*12
for month_index in range(0,12):
    #Define the relative monthly precipitation as a proportion of the monthly and yearly total
    seattle_relative_monthly_precipitation[month_index] = seattle_total_monthly_precipitation[month_index] / seattle_total_yearly_precipitation
    
#EXERCISE 1.4 & 2.3: Save the results to a json file
output_data = {
    'Seattle': {
        'station': 'GHCND:US1WAKG0038',
        'state': 'WA',
        'total_monthly_precipitation': seattle_total_monthly_precipitation,
        'total_yearly_precipitation': seattle_total_yearly_precipitation,
        'relative_monthly_precipitation': seattle_relative_monthly_precipitation
    }
}
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(output_data, file, indent=4)