from skills.core.file_handler import load, save
from skills.core.select_handler import phrase_sequencer
from skills.core.text_interpreter import find
from skills.core.settings import *


class Respond(object):

    _fields = [
        "scope",
        "cit_author",
    ]

    _arrays = [
        "standard_triggers",
        "standard_outputs",
        "power_triggers",
        "power_outputs",
        "avoid_triggers",
        "avoid_outputs",
    ]

    _counters = [
        "standard_counter",
        "power_counter",
        "avoid_counter"
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

        for field in self._fields:
            setattr(self, field, self.situational_reply[key].get(field, ""))
        for array in self._arrays:
            setattr(self, array, self.situational_reply[key].get(array, [""]))
        for counter in self._counters:
            setattr(self, counter, self.situational_reply[key].get(counter, 0))
        return

    def _set_reply_data(self, key):

        row = self.situational_reply[key]
        for field in self._fields:
            row[field] = getattr(self, field)
        for array in self._arrays:
            row[array] = getattr(self, array)
        for counter in self._counters:
            row[counter] = getattr(self, counter)
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
                if el[1] == STATIC_REPLAY and (mode is STD_REPLAY or POWER_REPLAY or STATIC_REPLAY):
                    return

        trigger = trigger.split(STATIC_SPLIT_KEY)
        # Look for the trigger
        if not find(trigger[0], self.text, starting_point):
            return

        # Delete the item cause there is something better with this key
        if el_index != -1:
            self.output.pop(el_index)


        sentence = [key]

        # save the static reply if founded
        if len(trigger) >= 2:
            sentence.append(STATIC_REPLAY)
            sentence.append(trigger[1])
            if len(trigger) > 2:
                sentence.append(" ".join(trigger[2].split()))
            else:
                sentence.append("")

        # create the avoid reply
        elif self._find_avoid():
            sentence.append(AVOID_REPLY)
            self.avoid_counter, out = phrase_sequencer(vet_outputs, self.avoid_counter)
            sentence.append(out)
            sentence.append("")

        # create the standard or power reply
        else:
            if mode is POWER_REPLAY:
                sentence.append(POWER_REPLAY)
                self.power_counter, out = phrase_sequencer(vet_outputs, self.power_counter)
                sentence.append(out)
                sentence.append(self.cit_author)
            else:
                sentence.append(STD_REPLAY)
                self.standard_counter, out = phrase_sequencer(vet_outputs, self.standard_counter)
                sentence.append(out)
                sentence.append("")

        #append to the output
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
