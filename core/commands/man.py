from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.command_reader import CommandReader
from core.src.static_modules import db
from core.src.text_reply.modules_reply_models import man_title, man_description, man_usage
from core.src.text_reply.errors import arg_not_found_error


class Man(object):
    """
    """

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.command = command
        self.arg = arg

        self.c_reader = CommandReader()

    def _build_man(self, language, command_name):

        try:
            self.c_reader.read_command(language, command_name)
            out = man_title(language, command_name, self.c_reader.invocation_word) + '\n'
            out += man_description(language, self.c_reader.description) + '\n'
            out += man_usage(language, self.c_reader.usage)
            return out
        except Exception as e:
            print(e)
            return e

    def man(self):

        out = ''

        if self.arg == 'all' or self.arg == '':
            for key in self.c_reader.commands_keys:
                out += self._build_man(self.language, key) + '\n\n'
        else:
            try:
                command_found, language_found = self.c_reader.find_command(db.guild.languages, self.arg)
            except Exception as e:
                print(e)
                return

            if command_found is None:
                out = arg_not_found_error(language_found)  # use guild main language
                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                return

            out = self._build_man(language_found, command_found)

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
