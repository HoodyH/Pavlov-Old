from telegram.parsemode import ParseMode
from telegram.bot import Bot
from telegram.update import Update

from static.configurations import logger, LOGGING_CHAT
from pvlv_database import Database, BaseStatsUpdater
from pvlv_img_builder.level_up_card import DrawLevelUpCard
from pvlv_commando import CommandExecutionFail, ManualExecutionFail
from pvlv_commando import Commando
com = Commando()


class BaseHandler(object):

    def __init__(self, update, bot):
        self.update: Update = update
        self.bot: Bot = bot

        # Unwrap all te data from the bot
        private = True if self.update.message.chat.type == 'private' else False
        chat_name = self.update.message.chat.title

        self.username = self.update.message.from_user.name if self.update.message.from_user.name else 'anonymous'

        self.guild_id = self.update.message.from_user.id
        self.guild_name = self.username if private else chat_name
        self.user_id = self.update.message.chat.id

        self.db = Database(self.guild_id, self.user_id)

        # Update the stats
        self.bsu = BaseStatsUpdater(self.db)
        self.bsu.timestamp(self.update.message.date)
        self.bsu.username(self.username)
        self.bsu.guild_name(self.guild_name)

    def check_level_up(self):
        if self.bsu.is_level_up:
            data = {
                'level': self.db.user.guild.xp.level,
                'bold_text': 'Congratulations User',
                'text': 'You have gained a level\nKeep like that',
            }
            d = DrawLevelUpCard(data)
            d.draw_level_up()
            self.update.message.reply_photo(d.get_image())

    def check_commands(self, text):

        if text.startswith('.'):

            logger.info('user: {} in {} sent {}'.format(
                self.update.message.from_user.name,
                self.update.message.chat.title,
                text
            ))

            try:
                # text without the command invocation word, and the language of the command
                com.find_command(text[1:], self.db.guild.languages[0], self.db.user.guild.permissions)

                """
                Send to the chat with parse mode enabled 
                ** mean bold
                - if your chat doesn't support parse mode use com.run_manual().replace('**', '')
                - if your chat has a different parse mode use com.run_manual().replace('**', 'your_format')
                """
                man = com.run_manual()
                if man:
                    self.update.message.reply_text(man.replace('**', '*'), parse_mode=ParseMode.MARKDOWN)

                com.run_command(self.update)  # here you have to pass the bot object that will be used

            # Do exception handling as you please
            except CommandExecutionFail as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
                logger.error(exc.error_report)
                self.bot.send_message(LOGGING_CHAT, exc.error_report)

            except ManualExecutionFail as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
                logger.error(exc.error_report)
                self.bot.send_message(LOGGING_CHAT, exc.error_report)

            except Exception as exc:
                self.update.message.reply_text(str(exc))  # the exception to send in chat
