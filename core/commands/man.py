from core.src.file_handler import load, save
from core.src.settings import *
from core.src.internal_log import Log
from core.src.text_reply.modules_reply_models import no_action_taken, mode_updated
from core.src.text_reply.errors import parse_error


class Man(object):
    """
    this command will mute the given module.
    """

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.command = command
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

    def man(self):
        return
