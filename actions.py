# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import requests as r
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email = tracker.get_slot('email')
        dispatcher.utter_message(text="Sent!")

        return []

class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('secrets.txt', 'r') as f:
            API_KEY = f.readline()

        location = tracker.get_slot('location')
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&units=imperial".format(location, API_KEY)

        response = r.get(url)
        response_json = r.json()
        weather = response_json['weather']
        description = response_json['weather'][0]['description']
        temperature = response_json['main']['temp']
        feels_like = response_json['main']['feels_like']
        humidity = response_json['main']['humidity']

        message = """Right now in {} you can expect {}. The temperature is {} degrees (F), but it feels like {} with {}% humidity""".format(location, description, temperature, feels_like, humidity)

        dispatcher.utter_message(text=message)

        return []