from core.src.static_modules import bestemmia
from core.src.message_reader import find

TRIGGER_LIST_LEN = 6

BASE_TRIGGERS_ITA = [
        ['dio', 'porco'],
        ['madonna'],
        ['troiaa'],
        ['puttana'],
        ['gesù', 'gesu'],
        ['allah', 'halla'],
    ]

BASE_TRIGGERS_ENG = [
        ['god'],
        ['madonna'],
        ['whore'],
        ['bitch'],
        ['jesus'],
        ['allah'],
    ]


class BestemmiaReply(object):

    def __init__(self):
        self.subject = None
        return

    def build_triggers(self, language, character_number):

        # build with standard calls

        if language == 'ita':
            triggers = BASE_TRIGGERS_ITA[character_number]
            self.subject = BASE_TRIGGERS_ITA[character_number][0]
        else:
            triggers = BASE_TRIGGERS_ENG[character_number]
            self.subject = BASE_TRIGGERS_ENG[character_number][0]

        return triggers

    def message_reply(self, language, text):

        # look for trigger words
        for i in range(0, TRIGGER_LIST_LEN):
            for trigger in self.build_triggers(language, i):
                if find(trigger, text):
                    return bestemmia.bestemmia(language, self.subject)

        return ""
