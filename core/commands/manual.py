from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.command_reader import CommandReader
from core.src.static_modules import db
from core.src.text_reply.reply_commands.man_reply import (
    invocation, handled_args, handled_params, command_mask
)
from core.src.text_reply.errors import arg_not_found_error


class Manual(object):
    """
    """

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.command = command
        self.arg = arg

        self.c_reader = CommandReader()

    def _build_title(self, command_function, command_name):
        out = '**{}**\n{}\n'.format(
            command_name.upper(),
            command_function.description,
        )
        inv = command_function.invocation_words
        if inv:
            out += '{}\n'.format(
                invocation(self.language, command_function.invocation_words)
            )
        return out

    def _build_args_params_list(self, title_function, dictionary):
        if dictionary != {}:
            out = '\n{}\n'.format(title_function(self.language))
            for key in dictionary.keys():
                key_description = dictionary.get(key)
                out += '**{}** -- {}\n'.format(
                    key if key != '' else 'void',
                    key_description
                )
            return out
        else:
            return ""

    def _build_full_man(self, command_name):

        try:
            self.c_reader.commands.read_command(self.language, command_name)
            out = self._build_title(self.c_reader.commands, command_name)
            out += self._build_args_params_list(handled_args, self.c_reader.commands.handled_args)
            out += self._build_args_params_list(handled_params, self.c_reader.commands.handled_params)
            return out

        except Exception as e:
            print(e)
            return e

    def _build_base_man(self, command_function, command_name):

        try:
            command_function.read_command(self.language, command_name)
            out = self._build_title(command_function, command_name)
            return out

        except Exception as e:
            print(e)
            return e

    def _print_found_command(self, command_function, command):
        try:
            command_name = command_function.key
            out = '{}\n{}'.format(
                self._build_title(command_function, command_name),
                command_mask(self.language, db.guild.prefix, command, command_function.sub_call)
            )
            return out

        except Exception as e:
            print(e)
            return e

    def manual(self):

        def void_arg():
            _out = ''
            if self.arg == '':
                _out = self._build_full_man('manual')
            return _out

        def all_commands():
            _out = ''
            for key in self.c_reader.commands.commands_keys:
                _out += '{}\n'.format(self._build_base_man(self.c_reader.commands, key))
            for key in self.c_reader.commands_shortcut.commands_shortcut_keys:
                _out += '{}\n'.format(self._build_base_man(self.c_reader.commands_shortcut, key))
            return _out

        def command_name():
            _out = ''
            try:
                l, command_found, t = self.c_reader.get_command(db.guild.languages, self.arg)
            except Exception as er:
                print(er)
                return

            if command_found is None:
                _out = arg_not_found_error(self.language)  # use guild main language
                self.bot.send_message(_out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                return ''

            if l is None:
                _out = self._build_full_man(command_found)
            else:
                _out = self._print_found_command(self.c_reader.commands_shortcut, command_found)

        chose = {
            '': void_arg,
            'all': all_commands,
        }

        try:
            out = chose[self.arg]()
        except Exception as e:
            out = command_name()
            print(e)
            return

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
