"""from old_core.src.utils.select_handler import random_between
"""

class Random(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        # parameter handed
        self._filter = None
        self._set = None

        _vars = ['filter', 'set']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def random(self):

        def void_arg():

            ppl = ['simone', 'mattia', 'luca', 'master', 'alberto', 'clock']
            out = ppl[random_between(0, len(ppl))]

            self.bot.send_message(out, MSG_ON_SAME_CHAT)

        chose = {
            '': void_arg,
        }

        chose[self.arg]()
