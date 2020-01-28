from pvlv.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.static_modules import db
from pvlv_image_builder.draw_levels import DrawLevelCard
from core.src.text_reply.reply_commands.level_reply import (
    text_description, text_description_global
)


class Level(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

    def level(self):

        def void_arg():
            _data = {
                'username': self.bot.user.username,
                'data': {
                    'rank': db.rank,
                    'rank_label': 'RANK',
                    'level': db.level,
                    'level_label': 'LEVEL',
                },
                'bar': {
                    'value': db.xp_gained_in_current_level,
                    'max': db.level_xp,
                },
                'text': text_description(self.language, db.level),
            }

            return _data

        def global_arg():
            _data = {
                'username': self.bot.user.username + ' (GLB)',
                'data': {
                    'rank': db.rank_global,
                    'rank_label': 'RANK',
                    'level': db.level_global,
                    'level_label': 'LEVEL',
                },
                'bar': {
                    'value': db.xp_gained_in_current_level_global,
                    'max': db.level_xp_global,
                },
                'text': text_description_global(self.language, db.level_global),
            }

            return _data

        chose = {
            '': void_arg,
            'global': global_arg,
        }

        try:
            data = chose[self.arg]()
        except Exception as e:
            print(e)
            return

        dl = DrawLevelCard(data)
        dl.draw_level_card()

        self.bot.send_image(dl.get_image(), MSG_ON_SAME_CHAT)

