# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.weather import get_weather
from actions.email_resume import email_resume


class ActionSendEmail(Action):

    def name(self) -> Text:
        return "action_email_resume"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        email = tracker.get_slot('email')
        email_resume(email)
        dispatcher.utter_message(text="Sent!")

        return []


class ActionGetWeather(Action):

    def name(self) -> Text:
        return "action_get_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot('location')
        message = get_weather(location)
        if message is None:
            dispatcher.utter_message(
                "Oops! Looks like the OpenWeatherAPI couldn't recognize that location. Try you like to try again? Try giving just the name of the city.")
            tracker.slots.clear()
        else:
            dispatcher.utter_message(text=message)

        return []
