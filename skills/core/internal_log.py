from skills.core.settings import *
from skills.core.file_handler import log_data
from skills.core.utils.formatting import time_now, mode_to_name


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
    def modules_handler_prefix(scope, guild_id, user_id, prefix):

        data = '[{}] "{}", On guid: <{}> user: <{}> has used <{}> prefix'.format(
            time_now(),
            scope.upper(),
            guild_id,
            user_id,
            prefix
        )
        log_data(data)
        print(data)
