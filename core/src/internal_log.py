from core.src.settings import *
from core.src.file_handler import log_data
from core.src.utils.internal_formatting import time_now, mode_to_name


class Log(object):

    @staticmethod
    def module_status_changed(scope, guild_id, user_id, module_name, old_module_status, new_module_status):

        data = '[{}] ""{}", On guid: <{}> user: <{}> has changed {} status from {} to {}.'.format(
            time_now(),
            scope.upper(),
            guild_id,
            user_id,
            " ".join(module_name.upper().split("_")),
            mode_to_name(old_module_status),
            mode_to_name(new_module_status)
        )
        log_data(data)
        print(data)

    @staticmethod
    def top_level_error(error, module_name):

        data = '[{}] Top level error in: {} {}'.format(
            time_now(),
            module_name.upper(),
            error
        )
        log_data(data)
        print(data)

    @staticmethod
    def message_reply_error(error_type, guild, trigger=None):

        if error_type is WRONG_STATIC_MODE_STRING:
            data = '[{}] On guid: <{}> Wrong syntax in trigger <{}>'.format(
                time_now(),
                guild,
                trigger,
                STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE, STATIC_SPLIT_MODE,
                STATIC_SPLIT_MODE, STATIC_SPAM_MODE, STATIC_SPLIT_MODE
            )
            log_data(data)
            print(data)

    @staticmethod
    def modules_handler_prefix(scope, guild, user, prefix):

        data = '[{}] "{}", <{}, {}> used <{}>'.format(
            time_now(),
            scope.upper(),
            guild,
            user,
            prefix
        )
        log_data(data)
        print(data)

    @staticmethod
    def command_log(scope, guild, user, prefix, command):
        data = '[{}] "{}", <{}, {}> used <{}{}>'.format(
            time_now(),
            scope.upper(),
            guild,
            user,
            prefix,
            command
        )
        log_data(data)
        print(data)

    @staticmethod
    def console_login_as(username, user_id):
        print("+-----------------------------------------")
        print("| Client successfully connected as:")
        print("| Username: {}\n| ID: {}".format(username, user_id))
        print("+-----------------------------------------")

    @staticmethod
    def console_user_action_log(username, user_id, action):
        print("+-----------------------------------------")
        print("| User {}[{}] at {}".format(username, user_id, time_now))
        print("| He has {}".format(action))
        print("+-----------------------------------------")

    @staticmethod
    def console_simple_action_log (action):
        print("+-----------------------------------------")
        print("| He has {}".format(action))
        print("+-----------------------------------------")
