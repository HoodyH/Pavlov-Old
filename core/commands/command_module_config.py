from core.src.file_handler import load, save
from core.src.settings import *
from core.src.internal_log import Log
from core.src.text_reply.modules_reply_models import no_action_taken, mode
from core.src.text_reply.errors import parse_error


class ModuleStatus(object):
    """
    this command will mute the given module.
    """

    def __init__(self, scope, guild_id, user_id, language, command, arg, params):

        self.language = language
        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id

        self.command_name = command
        self.arg = arg

        # parameter handed
        self._set = None
        self._l = None

        _vars = ['set', 'l']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        self._set_string = self._set
        try:
            self._set = int(self._set)
        except Exception as e:
            Log.top_level_error(e, "module config")
            self._set = ERROR

        # configuration file
        self.config = load(guild_id, scope, 'config')
        self.commands = load(guild_id, scope, 'commands')

    def _read_module_status(self):

        module = self.config.get('modules_status').get(self.arg)
        if module is None:
            self.enabled = 0
            self.mode = 0
            return
        self.enabled = module.get('enabled')
        self.mode = module.get('module_mode')
        return

    def _set_module_status(self):

        field = self.config['modules_status'][self.arg] = {}
        field['enabled'] = self.enabled
        field['module_mode'] = self.mode

        save(self.guild_id, self.scope, "config", self.config)

    def mute(self):

        self._read_module_status()

        old_status = self.mode

        if self._set is ERROR:
            return parse_error(self.language, self._set_string, "0, 1, 2, 3")
        out = no_action_taken(self.language)
        if self._set is not None:
            if self._set is DISABLED_MODE:
                self.mode = DISABLED_MODE
                out = mode(self.language, "DISABLED")
            if self._set is QUIET_MODE:
                self.mode = QUIET_MODE
                out = mode(self.language, "QUIET")
            if self._set is NORMAL_MODE:
                self.mode = NORMAL_MODE
                out = mode(self.language, "NORMAL")
            if self._set is SPAM_MODE:
                self.mode = SPAM_MODE
                out = mode(self.language, "SPAM")
        elif self.mode is NORMAL_MODE:
            self.mode = QUIET_MODE
            out = mode(self.language, "QUIET")
        else:
            self.mode = NORMAL_MODE
            out = mode(self.language, "NORMAL")

        Log.module_status_changed(self.scope, self.guild_id, self.user_id, self.arg, old_status, self.mode)
        self._set_module_status()

        return out
