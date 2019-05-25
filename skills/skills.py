from skills.core.module_handler import Module
from skills.core.settings import *
# listeners
from skills.modules.message_reply import Respond


class Analyze(object):

    def __init__(self, scope, guild, user_id):

        self.module = Module(scope, guild, user_id)

        self.scope = scope
        self.guild = guild
        self.user_id = user_id

    def analyze_message(self, text):

        prefix_type, text = self.module.find_prefix(text)

        # run commands if the prefix is a COMMAND_PREFIX
        if prefix_type is COMMAND_PREFIX:
            return self.module.run_command(text)

        # don't analyze long messages
        if len(text) > MEX_MAX_LENGTH:
            return

        if self.module.permissions_listener('message_reply', prefix_type):
            respond = Respond(text, self.scope, self.guild)
            return respond.message_reply()


