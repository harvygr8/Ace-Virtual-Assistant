import requests , _json
# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import requests, json

api_key =  '8f280a3ef75916db6478d2d920addf63'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Thane"


class WeatherApp:
    weather_keys=['show me the weather','weather','current temperature','temperature']
    def fetchWeatherLabel():
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            z = x["weather"]
            temp=str(current_temperature-273.15)
            return temp

    def fetchWeatherText():
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()   
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            w_list=[current_temperature,current_pressure,current_humidity]
            return w_list
