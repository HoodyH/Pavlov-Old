from core.src.settings import *
from core.src.message_reader import find
from API.badass_character.badass_character import JOHN_WICK, CHUCK_NORRIS


class BadAssCharacterCall(object):

    @staticmethod
    def message_reply(language, text):

        text_len = len(text.split())

        john_wick_triggers = ['john', 'wick', 'john wick', 'jon wick']
        chuck_norris_triggers = ['chuck', 'norris', 'chuck norris', 'cuck norris']

        # look for trigger words
        for i in range(0, text_len):
            for trigger in john_wick_triggers:
                if find(trigger, text, i):
                    return badass_character.badass_sentence(language, JOHN_WICK)

            for trigger in chuck_norris_triggers:
                if find(trigger, text, i):
                    return badass_character.badass_sentence(language, CHUCK_NORRIS)

        return ""
