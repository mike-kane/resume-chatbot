import requests as r


def get_weather(location):
    with open('secrets.txt', 'r') as f:
        api_key = f.readline()

    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=imperial".format(location, api_key)

    response = r.get(url)
    if response.status_code == 200:
        response_json = response.json()
        weather = response_json['weather']
        description = response_json['weather'][0]['description']
        temperature = response_json['main']['temp']
        feels_like = response_json['main']['feels_like']
        humidity = response_json['main']['humidity']

        message = """Right now in {} you can expect {}. The temperature is {} degrees (F), but it feels like {} with {}% humidity""".format(
            location, description, temperature, feels_like, humidity)
    else:
        message = None

    return message
