from core.src.static_modules import pickup_line
from core.src.message_reader import find


class PickupLineCall(object):

    @staticmethod
    def message_reply(language, text):

        text_len = len(text.split())

        john_wick_triggers = ['pick up', 'pickup', 'approccia', 'attaccala', 'fecondala']

        # look for trigger words
        for i in range(0, text_len):
            for trigger in john_wick_triggers:
                if find(trigger, text, i):
                    return pickup_line.pickup_sentence(language)

        return ""
