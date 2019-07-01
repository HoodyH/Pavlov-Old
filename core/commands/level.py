from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.static_modules import db
from core.src.img_draw.draw_levels import DrawLevels
from core.src.text_reply.reply_commands.level_reply import (
    user_field, text_description, text_description_global
)


class Level(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

    def level(self):

        def void_arg():
            _level = db.level
            _title = user_field(self.language, self.bot.user.username)
            _text = text_description(self.language, db.level)

            return _level, _title, _text

        def global_arg():
            _level = db.global_level
            _title = user_field(self.language, self.bot.user.username)
            _text = text_description_global(self.language, db.global_level)

            return _level, _title, _text

        chose = {
            '': void_arg,
            'global': global_arg,
        }

        try:
            level, title, text = chose[self.arg]()
        except Exception as e:
            print(e)
            return

        data = {
            'level': level,
            'title': title,
            'text': text,
        }

        dl = DrawLevels(data)
        dl.draw_level()

        self.bot.send_image(dl.get_image(), MSG_ON_SAME_CHAT)

