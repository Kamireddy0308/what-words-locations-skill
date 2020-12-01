from mycroft import MycroftSkill, intent_file_handler


class WhatWordsLocations(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('locations.words.what.intent')
    def handle_locations_words_what(self, message):
        self.speak_dialog('locations.words.what')


def create_skill():
    return WhatWordsLocations()

