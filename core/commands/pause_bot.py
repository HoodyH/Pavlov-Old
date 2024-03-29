from core.src.settings import (
    MSG_ON_SAME_CHAT,
    ENABLED, DISABLED
)
from core.src.static_modules import db
from core.src.text_reply.reply_commands.pause_bot_reply import response
from core.src.text_reply.errors import parse_error


class PauseBot(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language
        self.arg = arg

    def pause_bot(self):

        def enable():
            db.guild.bot_paused = True
            return response(self.language, DISABLED)

        def disable():
            db.guild.bot_paused = False
            self.bot.update_output_permission(False)
            return response(self.language, ENABLED)

        en_options = {
            ENABLED: disable,
            DISABLED: enable,
        }

        if self.arg == '':
            if db.guild.bot_paused:
                out = en_options[ENABLED]()
            else:
                out = en_options[DISABLED]()
            db.set_data()
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
        else:
            try:
                out = en_options[int(self.arg)]()
            except Exception as e:
                print(e)
                out = parse_error(self.language, self.arg, "0, 1")
            db.set_data()
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
