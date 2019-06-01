from skills.core.settings import *
from skills.core.interpreter_handler import find
from skills.core.internal_log import Log


ITA_STANDARD_CALLS = {
    "tira",
    "tira una",
    "tira un",
    "spara",
    "spara un",
    "spara una"
}

base_triggers = [
        ['dio', 'porco'],
        ['madonna'],
        ['troia'],
        ['puttana'],
        ['gesù', 'gesu'],
        ['allah', 'halla', 'alla']

    ]


class Bestemmia(object):

    def __init__(self, scope, guild_id, user_id, text, module_mode, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.text = text
        self.module_mode = module_mode
        self.prefix_mode = prefix_type

    def build_triggers(self, language, character_number):

        triggers = []

        # build with standard calls
        if language == 'ita':
            triggers = base_triggers[character_number].copy()
            for call in ITA_STANDARD_CALLS:
                for name in base_triggers[character_number]:
                    triggers.append('{} {}'.format(call, name))

        return triggers

    def message_reply(self, language):

        text_len = len(self.text.split())

        # look for trigger words
        for i in range(0, len(base_triggers)):
            for trigger in self.build_triggers(language, i):
                if find(trigger, self.text):
                    return bestemmia.bestemmia(language, base_triggers[i][0])

        return ""
