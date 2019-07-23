from core.src.settings import (
    MSG_ON_SAME_CHAT
)
from core.src.static_modules import db
from core.src.img_draw.draw_levels import DrawRanking
from core.src.text_reply.reply_commands.level_reply import (
    text_description, text_description_global
)


class Ranking(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

    def ranking(self):

        def build_ranking_dict(data):

            max_level_xp = db.calculate_xp_upto_level(data[1]['level'])
            for key in data.keys():
                data[key].update({
                    'level_label': 'LEVEL',
                    'max': int(max_level_xp),
                })
            return data

        def void_arg():

            db_data = db.ranking

            _data = {
                'title': 'Ranking of most Active Users',
                'title_color': (180, 180, 180),
                'rank': build_ranking_dict(db_data),
                'text': 'beta version'
            }

            return _data

        def global_arg():
            _data = {
                'username': self.bot.user.username + ' (GLB)',
                'data': {
                    'rank': db.rank,
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

        dr = DrawRanking(data)
        dr.draw_ranking()

        self.bot.send_image(dr.get_image(), MSG_ON_SAME_CHAT)
