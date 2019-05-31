from skills.core.file_handler import load, save
from skills.core.utils.select_handler import phrase_sequencer
from skills.core.interpreter_handler import find
from skills.core.settings import *
from skills.core.internal_log import Log


class Respond(object):

    _strings = [
        "name",
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

    _integers = [
        "enabled",
        "mode",
        "private",
        "standard_counter",
        "power_counter",
        "avoid_counter"
    ]

    def __init__(self, scope, guild_id, user_id, text, module_mode, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.text = text
        self.module_mode = module_mode
        self.prefix_mode = prefix_type

        self.situational_reply = load(self.guild_id, self.scope, "situational_reply")

        self.name = None
        self.enabled = None
        self.mode = None
        self.private = None
        self.users_allowed = None
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

    def _read_reply_data(self, key):

        for field in self._strings:
            setattr(self, field, self.situational_reply[key].get(field, ""))
        for array in self._arrays:
            setattr(self, array, self.situational_reply[key].get(array, [""]))
        for integer in self._integers:
            setattr(self, integer, self.situational_reply[key].get(integer, 0))
        self.users_allowed = self.situational_reply[key].get(self.scope, {self.scope: []}).get(self.scope, [])
        return

    def _set_reply_data(self, key):

        reply = self.situational_reply[key]
        for field in self._strings:
            reply[field] = getattr(self, field)
        for array in self._arrays:
            reply[array] = getattr(self, array)
        for integer in self._integers:
            reply[integer] = getattr(self, integer)
        try:
            reply["users_allowed"][self.scope] = self.users_allowed
        except Exception as e:
            Log.top_level_error(e, "message reply")
            reply["users_allowed"] = self.situational_reply[key].get(self.scope, {self.scope: self.users_allowed})
        save(self.guild_id, self.scope, "situational_reply", self.situational_reply)
        return

    def _find_avoid(self):

        for avoid in self.avoid_triggers:
            if find(avoid, self.text):
                return True
        return False

    def _find_trigger(self, trigger, vet_outputs, key, starting_point, output_type):


        # check if this key has already been used
        el_index = -1

        for el in self.output:
            if el[0] == key:
                el_index += 1
                if el[1] == AVOID_REPLY:
                    return
                if el[1] == STD_REPLAY and output_type == STD_REPLAY:
                    return
                if el[1] == POWER_REPLAY and (output_type is STD_REPLAY or POWER_REPLAY):
                    return
                if el[1] == STATIC_REPLAY and (output_type is STD_REPLAY or POWER_REPLAY or STATIC_REPLAY):
                    return

        # trigger permissions check
        if str.startswith(trigger, STATIC_SPLIT_MODE):

            trigger_array = trigger.split(STATIC_SPLIT_MODE)

            # the array must have 3 elements, or the user made an error writing it
            if len(trigger_array) is not 3:
                Log.message_reply_error(WRONG_STATIC_MODE_STRING, trigger)
                return

            # in case of override mode or in case of sudo (run)
            elif trigger_array[1] == STATIC_OVERRIDE_MODE and self.prefix_mode is (OVERRIDE_PREFIX or SUDO_PREFIX):
                trigger = trigger_array[2]

            # this trigger cant be used
            else:
                return

        trigger = trigger.split(STATIC_SPLIT_KEY)
        # Look for the trigger
        if not find(trigger[0], self.text, starting_point):
            return

        # Delete the item cause there is something better with this key
        if el_index != -1:
            self.output.pop(el_index)

        sentence = [key]
        # create the avoid reply
        if self._find_avoid():
            sentence.append(AVOID_REPLY)
            self.avoid_counter, out = phrase_sequencer(vet_outputs, self.avoid_counter)
            sentence.append(out)
            sentence.append("")

        # take the static reply if founded, but the avoid will be always checked
        elif len(trigger) >= 2:
            sentence.append(STATIC_REPLAY)
            sentence.append(trigger[1])
            if len(trigger) > 2:
                sentence.append(" ".join(trigger[2].split()))
            else:
                sentence.append("")

        # create the standard or power reply
        else:
            if output_type is POWER_REPLAY:
                sentence.append(POWER_REPLAY)
                self.power_counter, out = phrase_sequencer(vet_outputs, self.power_counter)
                sentence.append(out)
                sentence.append(self.cit_author)
            else:
                sentence.append(STD_REPLAY)
                self.standard_counter, out = phrase_sequencer(vet_outputs, self.standard_counter)
                sentence.append(out)
                sentence.append("")

        # append to the output
        self.output.append(sentence)
        self._set_reply_data(key)
        return

    def response_permissions_check(self):

        # sudo can run anything
        if self.prefix_mode is SUDO_PREFIX:
            return True

        # CHECK IF CAN BE RUN
        # check if this reply is enabled
        if self.enabled is False:
            return False

        # check if the user is allowed to call this key
        elif self.private is True and self.users_allowed.index(self.user_id) is None:
            return False

        # module is enabled
        else:
            # check if this reply can be run in this module mode
            if self.mode > self.module_mode:
                # everything can be run with the quiet prefix
                if self.prefix_mode is OVERRIDE_PREFIX:
                    return True
                return False

        return True

    def message_reply(self):

        text_len = len(self.text.split())

        for key in self.situational_reply.keys():

            self._read_reply_data(key)
            if self.response_permissions_check():

                # check all word in the sentence if contain triggers
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
