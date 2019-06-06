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
                "Messaggi Totali:": db.user.msg_total,
                "Tempo Sprecato:": sec_to_time(db.user.time_spent_sec, self.language)
            }
        else:
            dictionary = {
                "User Name:": db.user.user_name,
                "Total Messages:": db.user.msg_total,
                "Time Spent:": sec_to_time(db.user.time_spent_sec, self.language)
            }

        out = ''
        for key in dictionary.keys():
            out += '{} {}\n'.format(key, dictionary.get(key))

        return out
