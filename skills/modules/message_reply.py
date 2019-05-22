from skills.utils.file_handler import load
from skills.utils.select_handler import random_between
from skills.utils.interpreter import find


class Respond(object):
    
    global s_resp_global

    """
    it expects an array of words as input.
    """
    def __init__(self, text, scope, guild, **kwargs):

        self.text = text

        self.s_resp_json = load(guild, scope, "situational_reply")

        self.output_counter = None
        self.scope = None
        self.standard_triggers = None
        self.standard_outputs = None
        self.avoid_triggers = None
        self.avoid_outputs = None
        self.power_triggers = None
        self.power_outputs = None
        self.author = None

        self.output = []

    def _update_category(self, key):

        _vars = [
            "output_counter", 
            "scope", 
            "standard_triggers", 
            "standard_outputs", 
            "avoid_triggers", 
            "avoid_outputs", 
            "power_triggers",
            "power_outputs",
            "author",
        ]

        for var_name in _vars:
            setattr(self, var_name, self.s_resp_json[key].get(var_name, ""))

    def message_reply(self, word, word_index):

        def control(trigger, vet_outputs, key, mode):

            # ceck if this key has already been used in this mode
            el_index = -1
            for el in self.output:
                if el[0] == key:
                    el_index += 1
                    if el[1] == 0:
                        return
                    if el[1] == 1 and mode == "standard":
                        return
                    if el[1] == 2 and mode == "power":
                        return

            # Look for the key word
            if not find(trigger, self.text, word_index):
                return

            # Delete the item if there is something better
            if el_index != -1:
                self.output.pop(el_index)

            sentence = []
            sentence.append(key)
            if self.find_avoiders():
                sentence.append(0)
                sentence.append(self.avoid_outputs[random_between(0, len(self.avoid_outputs))])
                sentence.append("")
            else:
                if mode == "power":
                    sentence.append(2)
                else:
                    sentence.append(1)
                sentence.append(vet_outputs[random_between(0, len(vet_outputs))])
                sentence.append(self.author)

            self.output.append(sentence)
            return

        # look if there are the custom words
        for key in self.s_resp_json.keys():
            self._update_category(key)

            for trigger in self.standard_triggers: 
                control(trigger, self.standard_outputs, key, "standard")

            for trigger in self.power_triggers:  
                control(trigger, self.power_outputs, key, "power")
        return

    def find_avoiders(self):

        for avoider in self.avoid_triggers:
            if find(avoider, self.text):
                return True
        return False

    def get_reply(self):

        out = ""

        for el in self.output:
            out += "{}\n".format(str(el[2]))
            if el[3] != "":
                out += "cit. {}\n\n".format(str(el[3]))

        return out


