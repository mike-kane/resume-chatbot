import requests as r
import os


def get_weather(zipcode):

    api_key = os.environ['WEATHER_API_KEY']

    url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&APPID={}&units=imperial".format(zipcode, api_key)

    response = r.get(url)
    if response.status_code == 200:
        response_json = response.json()
        weather = response_json['weather']
        description = response_json['weather'][0]['description']
        temperature = response_json['main']['temp']
        feels_like = response_json['main']['feels_like']
        humidity = response_json['main']['humidity']

        message = """Right now in {} you can expect {}. The temperature is {} degrees (F), but it feels like {} with {}% humidity""".format(
            zipcode, description, temperature, feels_like, humidity)
    else:
        message = "API call failed! Status code: {}".format(response.status_code)

    return message
