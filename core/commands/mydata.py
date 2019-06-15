from core.src.settings import *
from core.src.static_modules import db
from core.src.text_reply.formatting import sec_to_time
from core.src.utils.img_draw import DrawImage
from datetime import datetime, timedelta


class MyData(object):
    """
    this command will mute the given module.
    """

    def __init__(self, scope, bot, guild_id, user_id, language, command, arg, params):

        self.scope = scope
        self.bot = bot
        self.guild_id = guild_id
        self.user_id = user_id
        self.language = language

        self.command_name = command
        self.arg = arg

    @staticmethod
    def _build_data(time_array, msg_array, time_spent_array, max_len, scope):

        timezone = 2
        data = [[], [], []]

        if scope == 'hour':
            now = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
        elif scope == 'day':
            now = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            now = datetime.utcnow()

        t = iter(time_array)
        el = next(t, None)
        for offset in range(0, max_len):

            def timedelta_scope():
                if scope == 'hour':
                    return timedelta(hours=offset)
                elif scope == 'day':
                    return timedelta(days=offset)
                else:
                    return timedelta(days=offset)

            def time_format_scope():
                if scope == 'hour':
                    return (n + timedelta(hours=timezone)).hour
                elif scope == 'day':
                    return (n + timedelta(hours=timezone)).day
                else:
                    return (n + timedelta(hours=timezone)).month

            n = (now - timedelta_scope())
            if el != n or el is None:
                data[0].append(time_format_scope())
                data[1].append(0)
                data[2].append(0)
            else:
                data[0].append(time_format_scope())
                i = time_array.index(el)
                data[1].append(msg_array[i])
                data[2].append(time_spent_array[i])
                el = next(t, None)
        return data

    def my_data_pro(self):

        data = {
            'HOURLY': self._build_data(
                db.user.msg.log_time_by_hour,
                db.user.msg.by_hour,
                db.user.msg.time_spent_by_hour,
                24,
                'hour'
                )
        }
        if len(db.user.msg.log_time_by_day) > 1:
            data['DAILY'] = self._build_data(
                db.user.msg.log_time_by_day,
                db.user.msg.by_day,
                db.user.msg.time_spent_by_day,
                7,
                'day'
            )
        if len(db.user.msg.log_time_by_month) > 1:
            data['MONTHLY'] = self._build_data(
                db.user.msg.log_time_by_month,
                db.user.msg.by_month,
                db.user.msg.time_spent_by_month,
                12,
                'month'
            )

        ds = DrawImage(data, db.user.user_name)
        ds.draw_msg_stats()
        img_bytes = ds.get_image()
        self.bot.send_photo(chat_id=self.guild_id if self.guild_id is not None else self.user_id, photo=img_bytes)

    def my_data(self):

        if self.arg.upper() == 'PRO':
            self.my_data_pro()
            return

        if self.language == ITA:
            dictionary = {
                "Nome Utente:": db.user.user_name,

                '\nRisultati Per ora:': '',
                "Messaggi Totali H:": db.user.msg.by_hour[0],
                "Tempo Sprecato H:\n": sec_to_time(db.user.msg.time_spent_by_hour[0], self.language),

                '\nRisultati Per Giorno:': '',
                "Messaggi Totali D:": db.user.msg.by_day[0],
                "Tempo Sprecato D:\n": sec_to_time(db.user.msg.time_spent_by_day[0], self.language),

                '\nRisultati Per Mese:': '',
                "Messaggi Totali M:": db.user.msg.by_month[0],
                "Tempo Sprecato M:\n": sec_to_time(db.user.msg.time_spent_by_month[0], self.language)
            }
        else:
            dictionary = {
                "User Name:": db.user.user_name,

                '\nResults this hour:': '',
                "Total Messages H:": db.user.msg.by_hour[0],
                "Time Spent H:\n": sec_to_time(db.user.msg.time_spent_by_hour[0], self.language),

                '\nResults this day:': '',
                "Total Messages D:": db.user.msg.by_day[0],
                "Time Spent D:\n": sec_to_time(db.user.msg.time_spent_by_day[0], self.language),

                '\nResults this month:': '',
                "Total Messages M:": db.user.msg.by_month[0],
                "Time Spent M:\n": sec_to_time(db.user.msg.time_spent_by_month[0], self.language)
            }

        out = ''
        for key in dictionary.keys():
            out += '{} {}\n'.format(key, dictionary.get(key))

        return out
