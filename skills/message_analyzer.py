
from skills.modules.simply_respond import respond

def find_match(text):
    for word in str(text).split():

        r = respond(word)
        if r is not None:
            return r
    return