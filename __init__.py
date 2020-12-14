from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from mycroft.util.log import LOG

class WhatWordsLocations(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('locations.words.what.intent')
    def handle_locations_words_what(self, message):
        getwordlist = message.data["wordlist"]
        splitwords = getwordlist.split(" ")
        joinwordformat = ".".join(splitwords)
        output = self.what_three_words(joinwordformat)
 
    def what_three_words(self, words):
        parameters = ['nearestPlace','country','square','coordinates']
        response = []
        url = 'https://api.what3words.com/v3/convert-to-coordinates?words={0}&key=4WBPDAOJ'.format(words)
        print(url)
        value = requests.get(url)
        json_value = value.json()
        try:
            for i in parameters:
                response.append(json_value[i])
            self.speak(response)
        except:
            self.speak("I didn't find any coordinates matching" + words)
        
def create_skill():
    return WhatWordsLocations()

