from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from mycroft.util.log import LOG

class WhatWordsLocations(MycroftSkill):
    def init(self):
        MycroftSkill.init(self)

    @intent_file_handler('locations.words.what.intent')
    def handle_locations_words_what(self, message):
        getwordlist = message.data["wordlist"]
        splitwords = getwordlist.split(" ")
        joinwordformat = ".".join(splitwords)
        output = self.what_three_words(joinwordformat)
 
    def what_three_words(self, words):
        url = 'https://api.what3words.com/v3/convert-to-coordinates?words={0}&key=4WBPDAOJ'.format(words)
        value = requests.get(url)
        json_value = value.json()
        try:
            response = json_value['nearestPlace']
            self.speak(response)
            response = json_value['country']
            self.speak(response)
            response = json_value['square']
            self.speak(response)
        except:
            self.speak("I didn't find any coordinates matching" + words)
        
def create_skill():
    return WhatWordsLocations()
