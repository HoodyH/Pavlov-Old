from pvlv_database import Database, BaseStatsUpdater
from pvlv_commando import CommandExecutionFail, ManualExecutionFail
from pvlv import com
from pvlv.static.configurations import logger


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
    def __init__(self, update, bot):
        self.__update = update
        self.__bot = bot

    def handle(self, guild_id, guild_name, user_id, username, timestamp, text: str):

        db = Database(guild_id, user_id)

        bsu = BaseStatsUpdater(guild_id, user_id, timestamp)
        bsu.text(text)
        bsu.username(username)
        bsu.guild_name(guild_name)
        bsu.update_text()

        """
        Check if there is the command prefix
        
        to do
        - find the command
        - check if the command is enabled in that particular chat or guild
        - check permissions for the command based on the used
        """
        if text.startswith('.'):
            logger.info('user: {} in {} sent {}'.format(username, guild_name, text))
            try:
                # text without the command invocation word, and the language of the command
                com.find_command(text[1:], db.guild.languages[0], db.user.guild.permissions)

                """
                Send to the chat with parse mode enabled 
                ** mean bold
                - if your chat doesn't support parse mode use com.run_manual().replace('**', '')
                - if your chat has a different parse mode use com.run_manual().replace('**', 'your_format')
                """
                man = com.run_manual()
                print(man) if man else None

                com.run_command(self.__update)  # here you have to pass the bot object that will be used

            # Do exception handling as you please
            except CommandExecutionFail as exc:
                self.__update.message.reply_text(str(exc))  # the exception to send in chat
                print(exc.error_report)  # the full report of the exception to send to a log chat or for internal log.

            except ManualExecutionFail as exc:
                self.__update.message.reply_text(str(exc))  # the exception to send in chat
                print(exc.error_report)  # the full report of the exception to send to a log chat or for internal log.

            except Exception as exc:
                self.__update.message.reply_text(str(exc))  # the exception to send in chat
