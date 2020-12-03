from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from mycroft.util.log import LOG

def what_three_words(words):
    url =
    print(url)
    value = requests.get(url)
    json_value = value.json()
    response = json_value['nearestPlace']
    return response

class WhatWordsLocations(MycroftSkill):
    def __int__(self):
        MycroftSkill.__init(self)

        @intent_file_handler('locations.words.what.intent')
        def handle_locations_words_what(self, message):
            getwordlist = message.data["wordlist"]
            splitwords = getwordlist.split(" ")
            joinwordformat = ".".join(splitwords)
            output = what_three_words(joinwordformat)
            self.speak(output)
def create_skill():
    return WhatWordsLocations()

