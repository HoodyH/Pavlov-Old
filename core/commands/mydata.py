from core.src.settings import *
from core.src.static_modules import db
from core.src.text_reply.formatting import sec_to_time, sec_to_time_short
from core.src.utils.img_draw import DrawGraph
from datetime import datetime, timedelta


class MyData(object):
    """
    this command will mute the given module.
    """

    def __init__(self, scope, bot, guild_id, user_id, username, language, command, arg, params):

        self.scope = scope
        self.bot = bot
        self.guild_id = guild_id
        self.user_id = user_id
        self.username = username
        self.language = language

        self.command_name = command
        self.arg = arg

    @staticmethod
    def __build_description(language, time_scope, n_messages, n_sec):

        if time_scope == 'hourly':
            if language == ITA:
                out = 'Questo grafico rappresenta i {} che hai inviato in queste ore\nPer un totali {} tempo sprecato.'
            else:
                out = 'This graph show the {} msg that\'s you\'ve sent in these hours\nFor a total of {} time wasted.'
        elif time_scope == 'daily':
            if language == ITA:
                out = 'Qui invece, puoi vedere i {} che hai inviato in questi giorni\nPer un totali {} tempo sprecato.'
            else:
                out = 'Here you can see the {} msg that\'s you\'ve sent in these days\n for a total of {} time wasted.'
        else:
            if language == ITA:
                out = 'In fine abbiamo i {} che hai inviato in questi mesi\nComplimenti, hai sprecato {} in tutto.'
            else:
                out = 'At the end we can see the {} msg sent in these months\nCongrats, {} wasted in total.'
        return out.format(n_messages, sec_to_time(n_sec, language))

    def __build_data(self, time_array, msg_array, time_spent_array, timezone, max_len, time_scope):

        data = [[], [], [], []]

        if time_scope == 'hourly':
            now = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
        elif time_scope == 'daily':
            now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            now = datetime.utcnow()

        t = iter(time_array)
        el = next(t, None)
        for offset in range(0, max_len):

            def timedelta_scope():
                if time_scope == 'hourly':
                    return timedelta(hours=offset)
                elif time_scope == 'daily':
                    return timedelta(days=offset)
                else:
                    return timedelta(days=offset)

            def time_format_scope():
                if time_scope == 'hourly':
                    return '{}h'.format((n + timedelta(hours=timezone)).hour)
                elif time_scope == 'daily':
                    return '{}h'.format((n + timedelta(hours=timezone)).day)
                else:
                    return '{}h'.format((n + timedelta(hours=timezone)).month)

            n = (now - timedelta_scope())
            if el != n or el is None:
                data[0].append(time_format_scope())
                data[1].append(0)
                data[2].append(0)
                data[3].append(sec_to_time_short(0))
            else:
                data[0].append(time_format_scope())
                i = time_array.index(el)
                data[1].append(msg_array[i])
                data[2].append(time_spent_array[i]/2)
                data[3].append(sec_to_time_short(time_spent_array[i]))
                el = next(t, None)

        i=1
        section = {
                'section_title': time_scope.upper(),
                'graph_1': {
                    'subtitle': 'Messages and Time spent here chatting',
                    'x_names': data[0],
                    'tower_1': {
                        'data': data[1],
                        'value_printed': data[1],
                        'printed_position': 'on_top',
                        'tower_dim': 1,
                        'color': DEFAULT_TOWER_1_COLOR
                    },
                    'tower_2': {
                        'data': data[2],
                        'value_printed': data[3],
                        'printed_position': 'on_top',
                        'tower_dim': 0.5,
                        'color': DEFAULT_TOWER_2_COLOR
                    },

                },
                'description': self.__build_description(self.language, time_scope, sum(data[1]), sum(data[2]))
            }

        return section

    def my_data_pro(self):

        timezone = 2

        dictionary_graph = {
            'top_title': self.username,
            'section_1': self.__build_data(
                db.user.msg.log_time_by_hour,
                db.user.msg.by_hour,
                db.user.msg.time_spent_by_hour,
                timezone,
                18,
                'hourly'
                )
        }

        if len(db.user.msg.log_time_by_day) > 2:
            dictionary_graph['section_2'] = self.__build_data(
                db.user.msg.log_time_by_day,
                db.user.msg.by_day,
                db.user.msg.time_spent_by_day,
                timezone,
                7,
                'daily'
            )

        if len(db.user.msg.log_time_by_month) > 1:
            dictionary_graph['section_3'] = self.__build_data(
                db.user.msg.log_time_by_month,
                db.user.msg.by_month,
                db.user.msg.time_spent_by_month,
                timezone,
                12,
                'monthly'
            )

        dg = DrawGraph(dictionary_graph)
        dg.draw_graph()
        img_bytes = dg.get_image()

        self.bot.send_photo(chat_id=self.guild_id if self.guild_id is not None else self.user_id, photo=img_bytes)

    def my_data(self):

        if self.arg.upper() == 'PRO':
            self.my_data_pro()
            return

        self.my_data_pro()
