from core.src.settings import (
    SUPPORTED_SCOPES, MSG_ON_SAME_CHAT
)
from core.src.static_modules import db
from core.src.text_reply.errors import (
    arg_void_not_allowed
)
from core.src.text_reply.formatting import time_to_string
from core.src.text_reply.reply_commands.communication_reply import (
    action_build, time_build,
    update_deploy_reply, update_competed_reply, update_test_reply, update_abort_reply,
    note_build
)


class Communication(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

        # parameter handed
        self.params = params
        self._t_start = None
        self._t_duration = None
        self._note = None
        self._note_ita = None

        _vars = ['t.start', 't.duration', 'note', 'note.ita']
        for param in params:
            name = '_{}'.format(param[0])
            setattr(self, name, param[1])

    def message_sender(self, function_message):
        for scope in SUPPORTED_SCOPES:
            db.iter_guild(scope)

            el = db.next_guild()
            while el is not None:
                out = '{}'.format(
                    function_message(db.language)
                )
                self.bot.send_message(out, el)
                el = db.next_guild()

    def communication(self):

        def void_arg():
            out = arg_void_not_allowed(self.language)
            self.bot.send_message(out, MSG_ON_SAME_CHAT)

        def update_deploy():

            def build_message(language):
                version = '0.7.12'
                action = action_build(language, 'update')
                if self._t_start is not None:
                    t_start = time_to_string(language, self._t_start, time_input='m')
                else:
                    t_start = time_to_string(language, 5, time_input='m')
                if self._t_duration is not None:
                    t_duration = time_to_string(language, self._t_duration, time_input='m')
                else:
                    t_duration = time_to_string(language, 20, time_input='m')
                note = note_build(language, self.params)
                out = '{}\n{}\n\n{}'.format(
                    update_deploy_reply(language, version),
                    time_build(language, action, time_to_start=t_start, time_duration=t_duration),
                    '' if note is None else note
                )

                return out

            self.message_sender(build_message)

        def update_completed():
            self.message_sender(update_competed_reply)

        def update_test():

            def build_message(language):
                version = '0.7.16'
                action = action_build(language, 'test')
                if self._t_start is not None:
                    t_start = time_to_string(language, self._t_start, time_input='m')
                else:
                    t_start = None
                if self._t_duration is not None:
                    t_duration = time_to_string(language, self._t_duration, time_input='m')
                else:
                    t_duration = time_to_string(language, 360, time_input='m')
                time = time_build(language, action, time_to_start=t_start, time_duration=t_duration)
                note = note_build(language, self.params)
                out = '{}\n\n{}'.format(
                    update_test_reply(language, version, time),
                    '' if note is None else note
                )
                return out

            self.message_sender(build_message)

        def update_abort():
            self.message_sender(update_abort_reply)

        chose = {
            "": void_arg,
            'update_deploy': update_deploy,
            'update_completed': update_completed,
            'update_test': update_test,
            'update_abort': update_abort,
        }

        chose[self.arg]()
