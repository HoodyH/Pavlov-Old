from skills.core.file_handler import load
from skills.core.interpreter_handler import find
from skills.core.settings import *
from skills.core.text_reply.errors import command_error, command_not_implemented
from skills.core.internal_log import Log

# commands
from skills.modules.admin.command_module_config import ModuleStatus
from skills.modules.telegram.mydata import MyData


class Module(object):

    def __init__(self, scope, guild_id, user_id):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.db = None

        self.config = load(scope, guild_id, "config")
        self.commands = load(scope, guild_id, "commands")

    def _read_configs(self):

        self.prefix = self.config.get('prefix')
        self.quiet_prefix = self.config.get('quiet_prefix')
        self.sudo_prefix = self.config.get('sudo_prefix')
        self.languages = self.config.get('languages')
        self.modules_status = self.config.get('modules_status')
        return

    def _read_commands(self, key, language):

        self.dm_enabled = self.commands[key].get('dm_enabled')
        self.permissions = self.commands[key].get('dm_enabled')
        self.invocation = self.commands[key][language].get('invocation')
        self.manual = self.commands[key][language].get('invocation')
        return

    def _execute_command(self, language, command, arg, params):
        """
        -execute the command code.
        """
        if command == "module.deactivate":
            return command_not_implemented(language)
        elif command == "module.status":
            m = ModuleStatus(self.scope, self.guild_id, self.user_id, language, command, arg, params)
            return m.mute()
        elif command == "insult":
            return command_not_implemented(language)
        elif command == "mydata":
            m = MyData(self.scope, self.guild_id, self.user_id, language, command, arg, params)
            return m.my_data()

    @staticmethod
    def _extract_value(input_array, starting_point=0):

        val = ""
        for j in range(starting_point, len(input_array)):
            # if is a input string
            if str.startswith(input_array[j], '-'):
                break
            if str.startswith(input_array[j], '"'):
                val += "{} ".format(input_array[j][1:])
            elif str.endswith(input_array[j], '"'):
                val += "{} ".format(input_array[j][:-1])
                break
            else:
                val += "{} ".format(input_array[j])
        if str.endswith(val, ' '):
            return val[:-1]
        else:
            return val

    def find_prefix(self, text):
        """
        :param text: input message
        :return: prefix type: COMMAND, SUDO, QUIET
        """

        self._read_configs()

        if str.startswith(text, self.prefix):
            text = text[len(self.prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user_id, self.prefix)
            prefix_type = COMMAND_PREFIX
        elif str.startswith(text, self.quiet_prefix):
            text = text[len(self.quiet_prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user_id, self.quiet_prefix)
            prefix_type = OVERRIDE_PREFIX
        elif str.startswith(text, self.sudo_prefix):
            text = text[len(self.sudo_prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user_id, self.sudo_prefix)
            prefix_type = SUDO_PREFIX
        else:
            prefix_type = NO_PREFIX
        return prefix_type, text

    def run_command(self, text):
        """
        :param text: input message
        :return: message response
        -read language/languages of the guild.
        -check if there's a command trigger or send an error.
        -extract arguments and parameters
        -run command
        -return response
        """
        if len(text) is 0:  # there was just the prefix
            return None

        text_array = text.split()

        command_found = None
        language_found = None

        # read language/languages of the guild.
        for language in self.languages:
            for command in self.commands.keys():
                self._read_commands(command, language)
                for trigger in self.invocation:
                    # check if there's a command trigger
                    if find(trigger, text_array[0]):
                        command_found = command
                        language_found = language

        # send an error
        if command_found is None:
            return command_error(self.languages[0])  # use guild main language

        # extract arguments and parameters
        arg = ""
        params = []
        text_array.pop(0)  # remove the command trigger
        for i in range(0, len(text_array)-1):
            if str.startswith(text_array[i], '-'):
                param_key = text_array[i][1:]
                param = [param_key]
                param_val = self._extract_value(text_array, i + 1)
                param.append(param_val)
                params.append(param)
            elif i is 0:
                arg = self._extract_value(text_array)

        # run command and return response
        return self._execute_command(language_found, command_found, arg, params)

    def permissions_listener(self, module_name, prefix_type):
        """
        check if there are the requisites to run the module (listener)
        """
        enabled = self.modules_status[module_name].get('enabled')
        mode = self.modules_status[module_name].get('mode')

        if prefix_type == SUDO_PREFIX:
            return True
        if enabled is DISABLED_MODE:
            return False
        if mode is DISABLED_MODE:
            return False
        if mode is QUIET_MODE and prefix_type == OVERRIDE_PREFIX:
            return True
        if mode is NORMAL_MODE or SPAM_MODE or AGGRESSIVE_MODE:
            return True
        return False
    
    def get_mode(self, module_name):
        return self.modules_status[module_name].get('mode')

    def get_guild_language(self):
        return self.languages[0]
