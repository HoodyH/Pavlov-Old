from core.src.settings import *
from core.src.static_modules import db
from core.src.file_handler import load_commands
from core.src.message_reader import find, extract_command_parameters
from core.src.text_reply.errors import command_error, command_not_implemented
from core.src.internal_log import Log
# listeners
from core.modules.user_data_log import UserDataLog
from core.modules.message_reply import Respond
from core.modules.bestemmia_call import BestemmiaCall
from core.modules.badass_character_call import BadAssCharacterCall
from core.modules.pickup_line_call import PickupLineCall
# commands
from core.commands.command_module_config import ModuleStatus
from core.commands.mydata import MyData


class User(object):
    def __init__(self, user_data):
        self.id = user_data.get('id')
        self.username = user_data.get('username')
        self.is_bot = user_data.get('is_bot')
        self.language_code = user_data.get('language_code')


class Chat(object):
    def __init__(self, chat_data):
        self.id = chat_data.get('id')
        self.title = chat_data.get('title')


class Starter(object):

    commands = load_commands()

    def __init__(self, scope, bot, message, message_data):
        """
        :param scope: string 'telegram' or 'discord'
        :param message_data: must be a dictionary with a predefined type of data set.
        """
        self.scope = scope
        self.bot = bot
        self.message = message
        self.guild_id = message_data.get('guild_id')
        self.guild_name = message_data.get('guild_name')
        self.date = message_data.get('date')
        self.message_id = message_data.get('message_id')
        self.chat = Chat(message_data.get('chat'))
        self.user = User(message_data.get('user'))
        self.text = message_data.get('text')
        self.message_type = message_data.get('message_type')

        # update db data
        db.update_data(self.scope, self.guild_id, self.user.id)

        self.prefix_type = NO_PREFIX
        self.module_enabled = 1
        self.module_mode = 1

        self.output = []

    def _catch_prefix(self):
        """
        fin and cut away the prefix
        """
        if str.startswith(self.text, db.guild.prefix):
            self.text = self.text[len(db.guild.prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user.id, db.guild.prefix)
            self.prefix_type = COMMAND_PREFIX

        elif str.startswith(self.text, db.guild.quiet_prefix):
            self.text = self.text[len(db.guild.quiet_prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user.id, db.guild.quiet_prefix)
            self.prefix_type = OVERRIDE_PREFIX

        elif str.startswith(self.text, db.guild.sudo_prefix):
            self.text = self.text[len(db.guild.sudo_prefix):]
            Log.modules_handler_prefix(self.scope, self.guild_id, self.user.id, db.guild.sudo_prefix)
            self.prefix_type = SUDO_PREFIX

        else:
            self.prefix_type = NO_PREFIX

    def _has_permissions(self, module_name):
        """
        check if there are the requisites to run the module (listener)
        """
        module = db.guild.modules.get(module_name)
        if module is None:
            field = db.guild.modules[module_name] = {}
            field['enabled'] = self.module_enabled
            field['module_mode'] = self.module_mode
            db.set_data()
        else:
            self.module_enabled = module.get('enabled')
            self.module_mode = module.get('module_mode')

        if self.prefix_type == SUDO_PREFIX:
            return True
        if self.module_enabled is DISABLED_MODE:
            return False
        if self.module_mode is DISABLED_MODE:
            return False
        if self.module_mode is QUIET_MODE and self.prefix_type == OVERRIDE_PREFIX:
            return True
        if self.module_mode is NORMAL_MODE or SPAM_MODE or AGGRESSIVE_MODE:
            return True
        return False

    def _read_command(self, key, language):

        self.dm_enabled = self.commands[key].get('dm_enabled')
        self.permissions = self.commands[key].get('permissions')
        self.invocation_word = self.commands[key][language].get('invocation_word')
        self.manual = self.commands[key][language].get('manual')

    def _run_command(self):
        """
        -read language/languages of the guild.
        -check if there's a command trigger or send an error.
        -extract arguments and parameters
        -run command
        -return response
        """
        __len = len(self.text)
        if len(self.text) is 0:  # there was just the prefix
            return

        text_array = self.text.split()

        command_found = None
        language_found = None

        # read language/languages of the guild.
        for language in db.guild.languages:
            for command in self.commands.keys():
                self._read_command(command, language)
                for trigger in self.invocation_word:
                    # check if there's a command trigger
                    if find(trigger, text_array[0]):
                        command_found = command
                        language_found = language

        # send an error
        if command_found is None:
            return command_error(db.guild.languages[0])  # use guild main language

        # extract arguments and parameters
        arg, params = extract_command_parameters(text_array)

        # run command and return response
        if command_found == "module.deactivate":
            return command_not_implemented(language_found)
        elif command_found == "module.status":
            m = ModuleStatus(self.scope, self.guild_id, self.user.id, language_found, command_found, arg, params)
            return m.mute()
        elif command_found == "mydata":
            m = MyData(self.scope, self.bot, self.guild_id, self.user.id, self.user.username, language_found, command_found, arg, params)
            return m.my_data()

    def analyze_message(self):

        self._catch_prefix()

        user_data_log = UserDataLog(
            self.scope,
            self.bot,
            self.guild_id,
            self.user.id,
            db.guild.languages[0],
            self.user.username,
            self.text,
            self.prefix_type
        )
        user_data_log.log_data()

        # run commands if the prefix is a COMMAND_PREFIX
        if self.prefix_type is COMMAND_PREFIX:
            c_out = self._run_command()
            return c_out

            # don't analyze long messages
        if len(self.text) > MEX_MAX_LENGTH:
            return None

        if self._has_permissions('message_reply'):
            respond = Respond(
                self.scope,
                self.guild_id,
                self.user.id,
                self.text,
                self.module_mode,
                self.prefix_type
            )
            self.output.append(respond.message_reply())

        if self._has_permissions('bestemmia_call'):
            bestemmia = BestemmiaCall()
            self.output.append(
                bestemmia.message_reply(db.guild.languages[0], self.text)
            )

        if self._has_permissions('badass_character_call'):
            badass_character_call = BadAssCharacterCall()
            self.output.append(
                badass_character_call.message_reply(db.guild.languages[0], self.text)
            )

        if self._has_permissions('pickup_line_call'):
            pickup_line_call = PickupLineCall()
            self.output.append(
                pickup_line_call.message_reply(db.guild.languages[0], self.text)
            )

        output = ""
        for el in self.output:
            if el != "":
                output += "\n{}".format(el)

        return output
