from pvlv_database import BaseStatsUpdater
from pvlv import com


class TextHandler(object):
    """
    Middle point to prepare data that have to be saved to the database
    This is an interface between the platform-wrapper and the pvlv_database

    This Handler will handle the operations on the text.
    Like:
     - stats updating
     - command reading
     - text interactions
    """
    def __init__(self, bot):
        self.__bot = bot

    def handle(self, guild_id, guild_name, user_id, username, timestamp, text):

        bsu = BaseStatsUpdater(guild_id, user_id, timestamp)
        bsu.text(text)
        bsu.username(username)
        bsu.guild_name(guild_name)
        bsu.update_text()

        if com.find_command(text[1:], 'eng'):
            com.run_command(self.__bot)
