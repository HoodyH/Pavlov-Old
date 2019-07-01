from core.src.settings import (
    ENG
)
from core.src.file_handler import load_commands, load_commands_shortcut
from core.src.message_reader import find

COMMANDS = load_commands()
COMMANDS_SHORTCUT = load_commands_shortcut()


class BaseCommandReader(object):
    def __init__(self):
        self._key = None
        self._invocation_words = None
        self._description = None

    @staticmethod
    def _read_language(language, module):
        module_language = module.get(language)
        if module_language is None:
            module_language = module.get(ENG)
            if module_language is None:
                raise Exception('There is not language descriptions in this command')
        return module_language

    def find_command(self, language_list, command_word, read_command_function, commands_keys):

        # read language/languages of the guild.
        for language in language_list:
            for command in commands_keys:
                read_command_function(language, command)
                if command == command_word:
                    return language, command
                for trigger in self._invocation_words:
                    # check if there's a command trigger
                    if find(trigger, command_word):
                        self._key = command
                        return language, command
        return None, None

    @property
    def key(self):
        return self._key

    @property
    def invocation_words(self):
        return self._invocation_words

    @property
    def description(self):
        return self._description


class CommandShortcutReader(BaseCommandReader):
    def __init__(self):
        super(CommandShortcutReader, self).__init__()
        self._dependency = None
        self._sub_call = None

    def read_command(self, language, module_name):

        module = COMMANDS_SHORTCUT.get(module_name)
        if module is None:
            raise Exception('Command: {} do not exist'.format(module))
        else:
            self._dependency = module.get('dependency')
            self._sub_call = module.get('sub_call')

            self._invocation_words = self._read_language(language, module.get('invocation_words'))
            self._description = self._read_language(language, module.get('description'))

    @property
    def dependency(self):
        return self._dependency

    @property
    def sub_call(self):
        return self._sub_call

    @property
    def commands_shortcut_keys(self):
        return COMMANDS_SHORTCUT.keys()


class CommandMainReader(BaseCommandReader):

    def __init__(self):
        super(CommandMainReader, self).__init__()
        self._management_command = None
        self._pro_command = None
        self._dm_enabled = None
        self._enabled_by_default = None
        self._permissions = None

        self._handled_args = None
        self._handled_params = None

    def _read_args_and_params(self, language, dictionary):
        result = {}
        for key in dictionary.keys():
            result[key] = self._read_language(language, dictionary.get(key))
        return result

    def read_command(self, language, module_name):

        module = COMMANDS.get(module_name)
        if module is None:
            raise Exception('Command: {} do not exist'.format(module))
        else:
            self._management_command = module.get('main_command')
            self._pro_command = module.get('pro_command')
            self._dm_enabled = module.get('dm_enabled')
            self._enabled_by_default = module.get('enabled_by_default')
            self._permissions = module.get('permissions')
            self._invocation_words = module.get('invocation_words')

            self._description = self._read_language(language, module.get('description'))
            self._handled_args = self._read_args_and_params(language, module.get('handled_args'))
            self._handled_params = self._read_args_and_params(language, module.get('handled_params'))

    @property
    def management_command(self):
        return self._management_command

    @property
    def pro_command(self):
        return self._pro_command

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
    def handled_args(self):
        return self._handled_args

    @property
    def handled_params(self):
        return self._handled_params

    @property
    def commands_keys(self):
        return COMMANDS.keys()


class CommandReader(object):
    def __init__(self):
        self._commands_shortcut = CommandShortcutReader()
        self._commands = CommandMainReader()

    def get_command(self, language_list, text):
        """
        :param language_list:
        :param text:
        :return:
        """

        if isinstance(text, list):
            text_array = text
        else:
            text_array = text.split()

        language_found, command_found = self._commands_shortcut.find_command(
            language_list,
            text_array[0],
            self._commands_shortcut.read_command,
            self._commands_shortcut.commands_shortcut_keys
        )
        if (command_found and language_found) is None:
            language_found, command_found = self._commands.find_command(
                language_list,
                text_array[0],
                self._commands.read_command,
                self._commands.commands_keys
            )
            language_found = None
        else:
            command_found = self._commands_shortcut.dependency
            self._commands.read_command(language_found, command_found)
            text_array = '{} {}'.format(command_found, self._commands_shortcut.sub_call).split()

        return language_found, command_found, text_array

    @property
    def commands_shortcut(self):
        return self._commands_shortcut

    @property
    def commands(self):
        return self._commands
