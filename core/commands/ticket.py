from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.utils.select_handler import random_between
from core.src.static_modules import db


class Ticket(object):

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

    def ticket(self):

        ticket = 'Tiket Opened by: @{}'.format(self.bot.user.username)

        out_admin = '{}\n\n{}'.format(ticket, self.arg)
        self.bot.send_message(out_admin, '338674622')

        out_user = '{}\n\nGrazie per la segnalazione.'.format(ticket)
        self.bot.send_message(out_user, MSG_ON_SAME_CHAT)


