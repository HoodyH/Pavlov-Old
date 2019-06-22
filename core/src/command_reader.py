from core.src.settings import (
    ENG
)
from core.src.file_handler import load_commands
from core.src.message_reader import find

COMMANDS = load_commands()


class CommandReader(object):

    def __init__(self):
        self._main_module = None
        self._dm_enabled = None
        self._enabled_by_default = None
        self._permissions = None
        self._invocation_word = None
        self._description = None
        self._usage = None
        self._handled_args = None
        self._handled_params = None
        self._man = None

    def read_command(self, language, module_name):

        module = COMMANDS.get(module_name)
        if module is None:
            raise Exception('Command: {} do not exist'.format(module))
        else:
            self._main_module = module.get('main_module')
            self._dm_enabled = module.get('dm_enabled')
            self._enabled_by_default = module.get('enabled_by_default')
            self._permissions = module.get('permissions')
            module_language = module.get(language)
            if module_language is None:
                module_language = module.get(ENG)
                if module_language is None:
                    raise Exception('There\'s not language descriptions in this command')

            self._invocation_word = module_language.get('invocation_word')
            self._description = module_language.get('description')
            self._usage = module_language.get('usage')
            self._handled_args = module_language.get('handled_args')
            self._handled_params = module_language.get('handled_params')
            self._man = module_language.get('man')

    def find_command(self, language_list, command_word):

        # read language/languages of the guild.
        for language in language_list:
            for command in COMMANDS.keys():
                try:
                    self.read_command(language, command)
                except Exception as e:
                    raise Exception(e)
                for trigger in self._invocation_word:
                    # check if there's a command trigger
                    if find(trigger, command_word):
                        return command, language
        return None, None

    @property
    def main_module(self):
        return self._main_module

    @property
    def dm_enabled(self):
        return self._dm_enabled

    @property
    def enabled_by_default(self):
        return self._enabled_by_default

    @property
    def permissions(self):
        return self._permissions

    @property
    def invocation_word(self):
        return self._invocation_word

    @property
    def description(self):
        return self._description

    @property
    def usage(self):
        return self._usage

    @property
    def handled_args(self):
        return self._handled_args

    @property
    def handled_params(self):
        return self._handled_params

    @property
    def man(self):
        return self._man

    @property
    def commands_keys(self):
        return COMMANDS.keys()

