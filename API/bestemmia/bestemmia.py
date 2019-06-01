from skills.core.file_handler import load, save
from skills.core.interpreter_handler import find
from skills.core.utils.select_handler import random_between
from data_global.static_text.bestemmia_data import *
from data_global.static_text.ITA.common_words import *
from skills.core.internal_log import Log


class Bestemmia(object):

    def __init__(self, scope, guild_id, user_id, text, module_mode, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.text = text
        self.module_mode = module_mode
        self.prefix_mode = prefix_type

        self.output = []

    def _find_trigger(self, trigger, vet_outputs, key, starting_point, ):

        if not find(trigger, self.text, starting_point):
            return

        sentence = [key]
        out = vet_outputs[random_between(0, len(vet_outputs)-1)]
        sentence.append('{} {}'.format(key, out))
        self.output.append(sentence)

    def message_reply(self):

        text_len = len(self.text.split())

        # build with standard calls
        madonna_triggers = MADONNA_TRIGGERS
        for el in STANDARD_CALLS:
            madonna_triggers.append('{} {}'.format(el, "madonna"))
        dio_triggers = DIO_TRIGGERS
        for el in STANDARD_CALLS:
            dio_triggers.append('{} {}'.format(el, "dio"))
            dio_triggers.append('{} {}'.format(el, "porco"))

        # look for trigger words
        for i in range(0, text_len):
            for trigger in madonna_triggers:
                self._find_trigger(trigger, MADONNA_FUNNY, 'Madonna', i)

            for trigger in dio_triggers:
                self._find_trigger(trigger, DIO_FUNNY, 'Dio', i)

        output = ""
        for el in self.output:
            print(el)
            output += "\n{}".format(str(el[1]))
        return output
