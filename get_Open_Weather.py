# get_Open_Weather.py - Prints weather forcast for a certain location


API_KEY = 'd89517fadb8b7fcd9c6d5ed18231cde3'

import json, requests
from datetime import datetime
from pytz import timezone


country_code = input('\nPlease input the two-letter country code: ')
state_code = input('\nPlease input the state code: ')
city_name = input('\nPlease input the city name: ')


# Download the JSON data from OpenWeatherMap.org's API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_KEY}'
response = requests.get(url)
response.raise_for_status()
weather_data = json.loads(response.text)

# convert timestamp to string
today_date_time =datetime.fromtimestamp(weather_data["dt"], tz=timezone('US/Pacific')).strftime('%A %b. %d, %Y %I:%M %p')

# Print weather descriptions:
print(today_date_time)
print(f'Current weather in {city_name}, {state_code}, {country_code}')
print(f'Current temperature: {(weather_data["main"]["temp"] - 273.15):.2f}C')
print(f'Current humidity: {weather_data["main"]["humidity"]}%')
