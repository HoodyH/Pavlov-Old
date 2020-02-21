from telegram.update import Update
from telegram.bot import Bot
from telegram.parsemode import ParseMode

from pvlv_database import Database
from .translations.help_reply import response


class Help(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.update: Update = bot[0]
        self.bot: Bot = bot[1]
        self.language = language

        self.db = Database(self.update.message.from_user.id, self.update.message.chat.id)

    def run(self):

        out = response(self.language, self.db.guild.prefix).replace('**', '*')
        self.update.message.reply_text(out, parse_mode=ParseMode.MARKDOWN)
