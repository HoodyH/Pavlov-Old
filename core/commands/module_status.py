from pvlv.settings import (
    DISABLED_MODE, QUIET_MODE, NORMAL_MODE, SPAM_MODE, AGGRESSIVE_MODE, ERROR,
    MSG_ON_SAME_CHAT,
    ENABLED, DISABLED
)
from core.src.static_modules import db
from core.src.internal_log import Log
from core.src.text_reply.reply_commands.module_status_reply import (
    no_action_taken, mode_updated, activation_status_update, not_a_module
)
from core.src.text_reply.errors import parse_error


class ModuleStatus(object):
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
        self._en = None

        _vars = ['set', 'en']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def mute(self):

        module = db.guild.modules.get(self.arg)
        if module is None:
            out = not_a_module(self.language, self.arg)
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return
        enabled = module.get('enabled')
        mode = module.get('module_mode')

        if self._set is ERROR:
            out = parse_error(self.language, self._set, "set 0, 1, 2, 3, 4")
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        if self._en is ERROR:
            out = parse_error(self.language, self._en, "en 0, 1")
            self.bot.send_message(out, MSG_ON_SAME_CHAT)
            return

        def disabled_mode():
            global mode
            mode = DISABLED_MODE
            return mode_updated(self.language, "DISABLED_MODE")

        def quiet_mode():
            global mode
            mode = QUIET_MODE
            return mode_updated(self.language, "QUIET_MODE")

        def normal_mode():
            global mode
            mode = NORMAL_MODE
            return mode_updated(self.language, "NORMAL_MODE")

        def spam_mode():
            global mode
            mode = SPAM_MODE
            return mode_updated(self.language, "SPAM_MODE")

        def aggressive_mode():
            global mode
            mode = AGGRESSIVE_MODE
            return mode_updated(self.language, "AGGRESSIVE_MODE")

        set_options = {
            DISABLED_MODE: disabled_mode,
            QUIET_MODE: quiet_mode,
            NORMAL_MODE: normal_mode,
            SPAM_MODE: spam_mode,
            AGGRESSIVE_MODE: aggressive_mode,
        }

        def enable():
            global enabled
            enabled = ENABLED
            return activation_status_update(self.language, self.arg, ENABLED)

        def disable():
            global enabled
            enabled = DISABLED
            return activation_status_update(self.language, self.arg, DISABLED)

        en_options = {
            DISABLED: disable,
            ENABLED: enable,
        }

        if (self._set or self._en) is not None:

            if self._set == '':
                old_mode = mode
                if mode is QUIET_MODE:
                    mode = NORMAL_MODE
                    out = set_options[NORMAL_MODE]()
                elif mode is QUIET_MODE:
                    mode = NORMAL_MODE
                    out = set_options[QUIET_MODE]()
                else:
                    mode = NORMAL_MODE
                    out = set_options[NORMAL_MODE]()

                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                Log.module_status_changed(
                    self.bot.scope,
                    self.bot.guild.id,
                    self.bot.user.id,
                    self.arg + "_mode",
                    old_mode,
                    mode
                )

            elif self._set is not None:
                old_mode = mode
                out = set_options[int(self._set)]()
                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                Log.module_status_changed(
                    self.bot.scope,
                    self.bot.guild.id,
                    self.bot.user.id,
                    self.arg + "_mode",
                    old_mode,
                    mode
                )

            if self._en == '':
                old_en = enabled
                if enabled is DISABLED:
                    enabled = ENABLED
                    out = en_options[ENABLED]()
                else:
                    enabled = DISABLED
                    out = en_options[DISABLED]()

                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                Log.module_status_changed(
                    self.bot.scope,
                    self.bot.guild.id,
                    self.bot.user.id,
                    self.arg + "_en",
                    old_en,
                    enabled
                )

            elif self._en is not None:
                old_en = enabled
                out = en_options[int(self._en)]()
                self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
                Log.module_status_changed(
                    self.bot.scope,
                    self.bot.guild.id,
                    self.bot.user.id,
                    self.arg + "_en",
                    old_en,
                    enabled
                )

            field = {
                'enabled': enabled,
                'module_mode': mode
            }
            db.guild.modules[self.arg] = field
            db.set_data()

        else:
            out = no_action_taken(self.language)
            self.bot.send_message(out, MSG_ON_SAME_CHAT, parse_mode_en=True)
