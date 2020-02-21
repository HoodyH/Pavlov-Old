from telegram.parsemode import ParseMode
from telegram.bot import Bot
from telegram.update import Update

from static.configurations import logger, LOGGING_CHAT
from pvlv_database import Database, BaseStatsUpdater
from pvlv_img_builder.level_up_card import DrawLevelUpCard
from handlers.level_up.level_up_reply import user_field, text_description
from pvlv_commando import CommandExecutionFail, ManualExecutionFail
from pvlv_commando import Commando

com = Commando()  # load all the the commands in the commands dir


class BaseHandler(object):
    """
    Middle point to prepare data that have to be saved to the database
    This is an interface between the platform-wrapper and the other modules

    This Handler will handle the operations on the text.
     - stats updating
     - command reading
     - text interactions
    """
    def __init__(self, update, bot):
        self.update: Update = update
        self.bot: Bot = bot

        # Unwrap all the data from the bot
        private = True if self.update.message.chat.type == 'private' else False
        chat_name = self.update.message.chat.title

        # some users can have the username not visible
        self.username = self.update.message.from_user.name if self.update.message.from_user.name else 'anonymous'

        self.guild_id = self.update.message.from_user.id
        # if the chat is direct to the bot set the guild name as username.
        self.guild_name = self.username if private else chat_name
        self.user_id = self.update.message.chat.id

        self.db = Database(self.guild_id, self.user_id)  # load database

        # Update the stats (this are standard for all type of messages)
        # The others stats must be set in the specific handler
        self.bsu = BaseStatsUpdater(self.db)
        self.bsu.timestamp(self.update.message.date)
        self.bsu.username(self.username)
        self.bsu.guild_name(self.guild_name)

    @property
    def is_bot_disabled(self):
        """
        if the guild is disabled,
        this means that the bot will ignore all the messages from that guild
        :return: the bot disable status
        """
        return self.db.guild.bot_disabled

    def check_level_up(self):
        """
        Check if the user has reached the xp to level up.
        If yes, send the level up chard in the same chat.
        The level up card has text, so in must be formatted based on the guild language
        """
        # check if the bot is paused in that guild
        if not self.db.guild.bot_paused:
            return

        if self.bsu.is_level_up:
            data = {
                'level': self.db.user.guild.xp.level,
                'bold_text': user_field(self.db.guild.languages[0], self.username),
                'text': text_description(self.db.guild.languages[0], self.db.user.guild.xp.level),
            }
            d = DrawLevelUpCard(data)
            d.draw_level_up()

            # Have level_up notifications enabled? then send in te chat
            if self.db.guild.level_up_notification:
                self.update.message.reply_photo(d.get_image())
            # else send it directly to the user
            else:
                self.bot.send_message(self.user_id, d.get_image())

    def check_commands(self, text):
        """
        Check if the text is a command.
        If yes execute it
        Here will be check:
        - the prefix handling (based on guild)
        - user permission to run the command
        - error handling, message error sending to log chat

        :param text: the text where search the command
        """

        if text.startswith('.'):
            log_message = 'user: <{}> in <{}> sent: <{}>'.format(
                    self.update.message.from_user.name,
                    self.update.message.chat.title,
                    text,
            )
            logger.info(log_message)

            try:
                # text without the command invocation word, and the language of the command
                com.find_command(text[1:], self.db.guild.languages[0], self.db.user.guild.permissions)

                # must be sent with parse mode enabled
                man = com.run_manual()
                if man:
                    # format fot respect the mark down code
                    self.update.message.reply_text(man.replace('**', '*'), parse_mode=ParseMode.MARKDOWN)

                # here you have to pass the bot object and the update obj that will be used
                com.run_command((self.update, self.bot))

            # Do exception handling as you please
            except CommandExecutionFail as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
                logger.error(exc.error_report)
                self.bot.send_message(LOGGING_CHAT, '{}\n\n{}'.format(log_message, exc.error_report))

            except ManualExecutionFail as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
                logger.error(exc.error_report)
                self.bot.send_message(LOGGING_CHAT, '{}\n\n{}'.format(log_message, exc.error_report))

            except Exception as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
