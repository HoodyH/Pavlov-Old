
from skills.utils.file_handler import load
from skills.utils.interpreter import find
from skills.settings import *
# MODULES
# listeners
from skills.modules.message_reply import Respond
# commands
from skills.manage.module_config import ModuleStatus

message_max_length = 70


class Analyze(object):

    def __init__(self, scope, guild, user_id):

        self.scope = scope
        self.guild = guild
        self.user_id = user_id

        self.config = load(scope, guild, "config")
        self.commands = load(scope, guild, "commands")

        self.prefix_mode = None

    def _get_config(self):

        self.prefix = self.config.get('prefix')
        self.quiet_prefix = self.config.get('quiet_prefix')
        self.sudo_prefix = self.config.get('sudo_prefix')
        self.languages = self.config.get('languages')
        self.modules_status = self.config.get('modules_status')
        return

    def _get_command(self, key, language):

        self.dm_enabled = self.commands[key].get('dm_enabled')
        self.permissions = self.commands[key].get('dm_enabled')
        self.invocation = self.commands[key][language].get('invocation')
        self.manual = self.commands[key][language].get('invocation')
        return

    def _run_command(self, command, arg, params):
        """
        -execute the command in the module.
        """
        if command == "module.deactivate":
            return
        elif command == "module.status":
            m = ModuleStatus(self.scope, self.guild, command, arg, params)
            return m.mute()
        elif command == "insult":
            return

    def _find_command(self, text):
        """
        -check if this is a command
        -read language/languages of the guild.
        -find if there's a command of send an error.
        """
        if not str.startswith(text, self.prefix):
            return None, None, None
        text_array = text[1:].split()
        _found_command = None

        for language in self.languages:
            for command in self.commands.keys():
                self._get_command(command, language)
                for trigger in self.invocation:
                    if find(trigger, text_array[0]):
                        _found_command = command

        if _found_command is None:
            return None, None, None

        def read_val(input_array, starting_point=0):

            val = ""
            for j in range(starting_point, len(input_array)):
                # if is a input string
                if str.startswith(input_array[j], '-'):
                    break
                if str.startswith(input_array[j], '"'):
                    val += "{} ".format(input_array[j][1:])
                elif str.endswith(text_array[j], '"'):
                    val += "{} ".format(input_array[j][:-1])
                    break
                else:
                    val += "{} ".format(input_array[j])
            if str.endswith(val, ' '):
                return val[:-1]
            else:
                return val

        params = []
        arg = ""
        text_array.pop(0)
        for i in range(0, len(text_array)):
            if str.startswith(text_array[i], '-'):
                param = []
                param_key = text_array[i][1:]
                param.append(param_key)
                param_val = read_val(text_array, i+1)
                param.append(param_val)
                params.append(param)
            elif i is 0:
                arg = read_val(text_array)

        return _found_command, arg, params

    def _find_prefix(self, text):

        # check the prefix executor type SUDO OR QUIET

        if str.startswith(text, self.quiet_prefix):
            text = text[1:]
            self.prefix_mode = QUIET_PREFIX
        if str.startswith(text, self.sudo_prefix):
            text = text[1:]
            self.prefix_mode = SUDO_PREFIX
        return text

    def _module_status(self, module_name):
        """
        -read in the appropriate json if the module is active
        """
        enabled = self.modules_status[module_name].get('enabled')
        status = self.modules_status[module_name].get('status')

        if self.prefix_mode == SUDO_PREFIX:
            return True
        if enabled is DISABLED:
            return False
        if status is DISABLED:
            return False
        if status is QUIET_MODE and self.prefix_mode == QUIET_PREFIX:
            return True
        if status is NORMAL_MODE:
            return True
        return False

    def analyze_message(self, text):

        self._get_config()

        # find commands
        command, arg, params = self._find_command(text)
        if command is not None:
            return self._run_command(command, arg, params)

        # check for a prefix (sudo or quiet)
        text = self._find_prefix(text)

        # don't analyze long messages
        if len(text) > message_max_length:
            return

        respond = Respond(text, self.scope, self.guild)
        if self._module_status('message_reply'):
            return respond.message_reply()


