# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

database = {
    "harry": {
        "account_number": "1234",
        "balance": 1000
    },
    "ron": {
        "account_number": "5678",
        "balance": 2500
    }
}

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "utter_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        account_number = tracker.get_slot("account_number")
        
        if name and account_number:
            if name in database and database[name]["account_number"] == account_number:
                balance = database[name]["balance"]
                dispatcher.utter_message(template="utter_check_balance", name=name, account_number=account_number, balance=balance)
            else:
                dispatcher.utter_message("Sorry, the provided details are incorrect.")
        else:
            dispatcher.utter_message("Sorry, I couldn't retrieve the balance. Please provide the necessary details.")

        return []
