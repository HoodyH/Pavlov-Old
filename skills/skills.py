from skills.core.modules_handler import Module
from skills.core.settings import *
# listeners
from skills.modules.user_data_log import UserDataLog
from skills.modules.message_reply import Respond
from skills.modules.bestemmia_call import Bestemmia
from skills.modules.badass_character_call import BadAssCharacterCall
from skills.modules.pickup_line_call import PickupLineCall


class Analyze(object):

    def __init__(self, scope, guild_id, guild_name, user_id, user_name):

        self.module = Module(scope, guild_id, user_id)

        self.scope = scope
        self.guild_id = guild_id
        self.guild_name = guild_name
        self.user_id = user_id
        self.user_name = user_name

        self.output = []

        db.update_data(self.scope, self.guild_id, self.user_id)

    def analyze_message(self, text):

        prefix_type, text = self.module.find_prefix(text)

        # run commands if the prefix is a COMMAND_PREFIX
        if prefix_type is COMMAND_PREFIX:
            return self.module.run_command(text)

        user_data_log = UserDataLog(
            self.scope,
            self.guild_id,
            self.user_id,
            self.user_name,
            text,
            prefix_type
        )
        user_data_log.log_data()

        # don't analyze long messages
        if len(text) > MEX_MAX_LENGTH:
            return None

        if self.module.permissions_listener('message_reply', prefix_type):
            respond = Respond(
                self.scope,
                self.guild_id,
                self.user_id,
                text,
                self.module.get_mode('message_reply'),
                prefix_type
            )
            self.output.append(respond.message_reply())

        if self.module.permissions_listener('bestemmia_reply', prefix_type):
            bestemmia = Bestemmia(
                self.scope,
                self.guild_id,
                self.user_id,
                text,
                self.module.get_mode('bestemmia_reply'),
                prefix_type
            )
            self.output.append(bestemmia.message_reply(self.module.get_guild_language()))

        if self.module.permissions_listener('badass_character_call', prefix_type):
            badass_character_call = BadAssCharacterCall(
                self.scope,
                self.guild_id,
                self.user_id,
                text,
                self.module.get_mode('badass_character_call'),
                prefix_type
            )
            self.output.append(badass_character_call.message_reply(self.module.get_guild_language()))

        if self.module.permissions_listener('pickup_line_call', prefix_type):
            pickup_line_call = PickupLineCall(
                self.scope,
                self.guild_id,
                self.user_id,
                text,
                self.module.get_mode('pickup_line_call'),
                prefix_type
            )
            self.output.append(pickup_line_call.message_reply(self.module.get_guild_language()))

        output = ""
        for el in self.output:
            if el != "":
                output += "\n{}".format(el)

        return output

