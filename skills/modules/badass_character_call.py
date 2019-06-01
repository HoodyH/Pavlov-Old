from skills.core.settings import *
from skills.core.interpreter_handler import find
from API.badass_character.badass_character import JOHN_WICK, CHUCK_NORRIS
from skills.core.internal_log import Log


class BadAssCharacterCall(object):

    def __init__(self, scope, guild_id, user_id, text, module_mode, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.text = text
        self.module_mode = module_mode
        self.prefix_mode = prefix_type

        self.output = []

    def message_reply(self, language):

        text_len = len(self.text.split())

        john_wick_triggers = ['john', 'wick', 'john wick', 'jon wick']
        chuck_norris_triggers = ['chuck', 'norris', 'chuck norris', 'cuck norris']

        # look for trigger words
        for i in range(0, text_len):
            for trigger in john_wick_triggers:
                if find(trigger, self.text, i):
                    return badass_character.badass_sentence(language, JOHN_WICK )

            for trigger in chuck_norris_triggers:
                if find(trigger, self.text, i):
                    return badass_character.badass_sentence(language, CHUCK_NORRIS)

        return ""
