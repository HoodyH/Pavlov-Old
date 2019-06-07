from core.src.settings import *
from core.src.text_reply.formatting import sec_to_time


class MyData(object):
    """
    this command will mute the given module.
    """

    def __init__(self, scope, guild_id, user_id, language, command, arg, params):

        self.language = language
        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id

        self.command_name = command
        self.arg = arg

    def my_data(self):

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
