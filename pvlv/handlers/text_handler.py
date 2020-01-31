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
    def __init__(self, update):
        self.__update = update

    def handle(self, guild_id, guild_name, user_id, username, timestamp, text: str):

        bsu = BaseStatsUpdater(guild_id, user_id, timestamp)
        bsu.text(text)
        bsu.username(username)
        bsu.guild_name(guild_name)
        bsu.update_text()

        """
        Check if there is the command prefix
        
        to do
        - find the command
        - controll if the command is enabled in that particular chat or guild
        - controll permissions for the command based on the used
        """
        if text.startswith('.'):
            try:
                com.find_command(text[1:], 'eng')
                com.run_command(self.__update)
            except Exception as exc:
                print(exc)
                self.__update.message.reply_text(com.error)
