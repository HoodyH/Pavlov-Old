from pvlv_database import Database
"""from old_core.src.text_reply.reply_commands.help_reply import response
"""

class Help(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

    def help(self):

        out = response(self.language, db.guild.prefix)
        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
