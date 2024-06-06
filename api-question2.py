from datetime import datetime
import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast?'

API_KEY = 'hidden'
CITY = "Jakarta"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
print(url)
response= requests.get(url)
data = response.json()
# print(data)

print("Weather forecasts:")

next_day=[0,8,16,24,32,39]
for i in next_day:
    temperature = data['list'][i]["main"]['temp']
    for_date = data['list'][i]["dt_txt"]
    my_date = datetime.strptime(for_date, '%Y-%m-%d %H:%M:%S')

    month_name = my_date.strftime('%b')  # %B for full month name
    day_name = my_date.strftime('%a')  # %B for full month name
    exact_date = my_date.strftime('%d')
    year = my_date.strftime('%Y')  # %B for full month name


    temperature_in_c = temperature - 273.15
    print(f"{day_name}, {exact_date} {month_name} {year}: {temperature_in_c:.2f} {chr(176)}C")
# format fri,23 apr 2020:16.72 celcius

    
    
