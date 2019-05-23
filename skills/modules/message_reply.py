from skills.utils.file_handler import load, save
from skills.utils.select_handler import random_between
from skills.utils.interpreter import find
from skills.settings import *


class Respond(object):

    _vars = [
        "scope",
        "standard_triggers",
        "standard_counter",
        "standard_outputs",
        "power_triggers",
        "power_counter",
        "power_outputs",
        "avoid_counter",
        "avoid_triggers",
        "avoid_outputs",
        "cit_author",
    ]

    def __init__(self, text, scope, guild):

        self.text = text
        self.scope = scope
        self.guild = guild

        self.situational_reply = load(self.guild, self.scope, "situational_reply")

        self.scope = None
        self.standard_triggers = None
        self.standard_counter = None
        self.standard_outputs = None
        self.power_triggers = None
        self.power_counter = None
        self.power_outputs = None
        self.avoid_counter = None
        self.avoid_triggers = None
        self.avoid_outputs = None
        self.cit_author = None

        self.output = []

    def _get_reply_data(self, key):

        for var_name in self._vars:
            setattr(self, var_name, self.situational_reply[key].get(var_name, 0))
        return

    def _set_reply_data(self, key):

        field = self.situational_reply[key]
        for var_name in self._vars:
            field[var_name] = getattr(self, var_name)
        save(self.guild, self.scope, "situational_reply", self.situational_reply)
        return

    def _find_avoid(self):

        for avoid in self.avoid_triggers:
            if find(avoid, self.text):
                return True
        return False

    def _find_trigger(self, trigger, vet_outputs, key, starting_point, mode):

        # check if this key has already been used
        el_index = -1

        for el in self.output:
            if el[0] == key:
                el_index += 1
                if el[1] == AVOID_REPLY:
                    return
                if el[1] == STD_REPLAY and mode == STD_REPLAY:
                    return
                if el[1] == POWER_REPLAY and (mode is STD_REPLAY or POWER_REPLAY):
                    return

        # Look for the keyword
        if not find(trigger, self.text, starting_point):
            return

        # Delete the item if there is something better
        if el_index != -1:
            self.output.pop(el_index)

        sentence = [key]
        if self._find_avoid():
            sentence.append(AVOID_REPLY)
            sentence.append(self.avoid_outputs[self.avoid_counter])
            sentence.append("")
            self.avoid_counter += 1
        else:
            if mode is POWER_REPLAY:
                sentence.append(POWER_REPLAY)
                sentence.append(vet_outputs[self.power_counter])
                sentence.append(self.cit_author)
                self.power_counter += 1
            else:
                sentence.append(STD_REPLAY)
                sentence.append(vet_outputs[self.standard_counter])
                sentence.append("")
                self.standard_counter += 1

        self.output.append(sentence)
        self._set_reply_data(key)
        return

    def message_reply(self):

        text_len = len(self.text.split())
        for key in self.situational_reply.keys():
            self._get_reply_data(key)

            for i in range(0, text_len):
                for trigger in self.standard_triggers:
                    self._find_trigger(trigger, self.standard_outputs, key, i, STD_REPLAY)

                for trigger in self.power_triggers:
                    self._find_trigger(trigger, self.power_outputs, key, i, POWER_REPLAY)

        output = ""
        for el in self.output:
            output += "\n\n{}".format(str(el[2]))
            if el[3] is not "":
                output += "\ncit. {}".format(str(el[3]))
        return output



