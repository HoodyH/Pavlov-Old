from skills.core.settings import *
from skills.core.interpreter_handler import find
from skills.core.internal_log import Log


class PickupLineCall(object):

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

        john_wick_triggers = ['pick up', 'pickup', 'approccia', 'attaccala', 'fecondala']

        # look for trigger words
        for i in range(0, text_len):
            for trigger in john_wick_triggers:
                if find(trigger, self.text, i):
                    return pickup_line.pickup_sentence(language)

        return ""
