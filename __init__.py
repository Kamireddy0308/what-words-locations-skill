from mycroft import MycroftSkill, intent_file_handler
import requests
import json
from mycroft.utils.log import getLogger

LOGGER = getLogger(_name_)
def what_three_words():
    x = 'task'
    y = 'exile'
    z = 'sorround'
    value = requests.get(
        'https://api.what3words.com/v3/convert-to-coordinates?words=' + x + '.' + y + '.' + z + '&key=4WBPDAOJ',
        verify=False)
    json_value = value.json()
    response = json_value['nearestPlace']
    return response

class WhatWordsLocations(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('locations.words.what.intent')
    def handle_locations_words_what(self, message):
        output = what_three_words()
        LOGGER.debug(message)
        self.speak_dialog(output)
        #self.speak_dialog('locations.words.what')


def create_skill():
    return WhatWordsLocations()

