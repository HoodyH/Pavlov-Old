from skills.utils.file_handler import loadJson
from skills.utils.random_handler import random_between

default_responds = loadJson("simply_responds")

    
def respond(msg):

    for key in default_responds.keys():
        for word in str(msg).split():
            if key.upper() == word.upper():
                print(word)
                array = default_responds[key]
                return default_responds[key][random_between(0, len(default_responds[key]))]
    return None


def add_respond(trigger, respond):
    return


def greatings(type):
    return

