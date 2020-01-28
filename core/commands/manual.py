from pvlv.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.command_reader import CommandReader
from core.src.static_modules import db
from core.src.text_reply.reply_commands.man_reply import (
    invocation, beta, handled_args, handled_params, command_mask
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

        self.cr = CommandReader()

    def _build_title(self, command_function, command_name):
        out = '**{}**\n{}\n'.format(
            command_name.upper(),
            command_function.description,
        )
        if command_function.invocation_words:
            out += '{}\n'.format(
                invocation(self.language, command_function.invocation_words)
            )
        if command_function.beta_command:
            out += '\n{}\n'.format(
                beta(self.language)
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
            self.cr.commands.read_command(self.language, command_name)
            out = self._build_title(self.cr.commands, command_name)
            out += self._build_args_params_list(handled_args, self.cr.commands.handled_args)
            out += self._build_args_params_list(handled_params, self.cr.commands.handled_params)
            return out

        except Exception as e:
            print(e)
            return e

    def _build_base_man(self, command_function, command_name):

        try:
            command_function.read_command(self.language, command_name)
            if not command_function.permissions > db.user.permissions:
                return self._build_title(command_function, command_name)
            else:
                return ""
        except Exception as e:
            print(e)

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

    def command_name(self):
        _out = ''
        try:
            l, command_found, t = self.cr.get_command(db.guild.languages, self.arg)
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
            _out = self._print_found_command(self.cr.shortcuts, command_found)

        return _out

    def void_arg(self):
        _out = ''
        if self.arg == '':
            _out = self._build_full_man('manual')
        return _out

    def all_commands(self):
        _out = ''
        for key in self.cr.commands.commands_keys:
            _out += '{}\n'.format(self._build_base_man(self.cr.commands, key))
        for key in self.cr.shortcuts.shortcuts_keys:
            _out += '{}\n'.format(self._build_base_man(self.cr.shortcuts, key))
        return _out

    def manual(self):

        chose = {
            '': self.void_arg,
            'all': self.all_commands,
        }

        try:
            out = chose[self.arg]()
        except Exception as e:
            out = self.command_name()
            print(e)

        self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
