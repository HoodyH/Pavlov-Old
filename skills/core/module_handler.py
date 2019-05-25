from skills.core.file_handler import load
from skills.core.text_interpreter import find
from skills.core.settings import *
from skills.core.utils.errors import command_error, command_not_implemented

# commands
from skills.admin.module_config import ModuleStatus


class Module(object):

    def __init__(self, scope, guild, user_id):

        self.scope = scope
        self.guild = guild
        self.user_id = user_id
        self.db = None

        self.config = load(scope, guild, "config")
        self.commands = load(scope, guild, "commands")

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
            m = ModuleStatus(self.scope, self.guild, command, arg, params)
            return m.mute()
        elif command == "insult":
            return command_not_implemented(language)

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
            text = text[1:]
            prefix_type = COMMAND_PREFIX
        elif str.startswith(text, self.quiet_prefix):
            text = text[1:]
            prefix_type = QUIET_PREFIX
        elif str.startswith(text, self.sudo_prefix):
            text = text[1:]
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
        status = self.modules_status[module_name].get('status')

        if prefix_type == SUDO_PREFIX:
            return True
        if enabled is DISABLED_MODE:
            return False
        if status is DISABLED_MODE:
            return False
        if status is QUIET_MODE and prefix_type == QUIET_PREFIX:
            return True
        if status is NORMAL_MODE:
            return True
        return False
