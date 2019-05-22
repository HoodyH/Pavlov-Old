from skills.utils.file_handler import load, save
from skills.settings import *


class ModuleStatus(object):
    """
    this command will mute the given module.
    """

    def __init__(self, guild, scope, command, arg, params):
        self.guild = guild
        self.scope = scope
        self.command_name = command
        self.arg = arg
        # parameter handed
        self._set = None
        self._l = None

        _vars = ['set', 'l']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

        # configuration file
        self.config = load(guild, scope, 'config')
        self.commands = load(guild, scope, 'commands')

    def _get_modules_status(self):

        module = self.config.get('modules_status').get(self.arg)
        if module is None:
            self.enabled = 0
            self.status = 0
            return
        self.enabled = module.get('enabled')
        self.status = module.get('status')
        return

    def _set_modules_status(self):

        field = self.config['modules_status'][self.arg] = {}
        field['enabled'] = self.enabled
        field['status'] = self.status

        save(self.guild, self.scope, "config", self.config)

    def mute(self):

        self._get_modules_status()
        print(self.enabled)
        out = "no action taken"
        if self._set is not None:
            if self._set is DISABLED:
                self.status = DISABLED
                out = "module DISABLED"
            if self._set is QUIET_MODE:
                self.status = QUIET_MODE
                out = "QUIET_MODE on"
            if self._set is NORMAL_MODE:
                self.status = NORMAL_MODE
                out = "NORMAL_MODE on"

        if self.status is NORMAL_MODE:
            self.status = QUIET_MODE
            out = "QUIET_MODE on"
        else:
            self.status = NORMAL_MODE
            out = "NORMAL_MODE on"

        self._set_modules_status()
        return out
