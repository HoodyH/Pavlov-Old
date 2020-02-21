from telegram.update import Update
from telegram.bot import Bot

from pvlv.settings import (
    ENABLED, DISABLED
)
from pvlv_database import Database
from .translations.pause_bot_reply import response


class PauseBot(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.update: Update = bot[0]
        self.bot: Bot = bot[1]
        self.language = language

        self.db = Database(self.update.message.from_user.id, self.update.message.chat.id)

    def __enable(self):
        self.db.guild.bot_paused = True
        return response(self.language, DISABLED)

    def __disable(self):
        self.db.guild.bot_paused = False
        return response(self.language, ENABLED)

    def run(self):

        # check the current bot status, and toggle the status
        if self.db.guild.bot_paused:
            out = self.__disable()
        else:
            out = self.__enable()

        self.update.message.reply_text(out)
