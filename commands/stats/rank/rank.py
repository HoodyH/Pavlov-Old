class Ranking(object):

    def __init__(self, bot, language, command, arg, params, *args, **kwargs):

        self.bot = bot
        self.language = language

        self.arg = arg

    def ranking(self):

        def build_ranking_dict(db_data, title):

            max_level_xp = db.calculate_xp_upto_level(db_data[1]['level'])
            for key in db_data.keys():
                db_data[key].update({
                    'level_label': 'LEVEL',
                    'max': int(max_level_xp),
                })

            _data = {
                'title': title,
                'title_color': (180, 180, 180),
                'rank': db_data,
                'text': 'beta2 version'
            }
            return _data

        def void_arg():
            db_data = db.ranking
            return build_ranking_dict(db_data, 'Ranking of most Active Users')

        def global_arg():
            db_data = db.ranking_global
            return build_ranking_dict(db_data, 'Ranking of most Active Users (Global)')

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
