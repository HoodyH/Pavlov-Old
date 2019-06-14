from core.src.settings import *


class MessageSender(object):
    def __init__(self, scope, bot, guild_id, user_id, channel_id):

        self.scope = scope
        self.bot = bot
        self.guild_id = guild_id
        self.user_id = user_id
        self.channel_id = channel_id

    def send_message(self, message, destination, user_tag=None):

        if self.scope == DISCORD:
            return

        elif self.scope == TELEGRAM:

            if destination == MSG_ON_STATIC_CHAT:
                self.bot.send_message(chat_id=self.channel_id, text=message)
            elif destination == MSG_ON_SAME_CHAT:
                self.bot.send_message(chat_id=self.channel_id, text=message)
            else:
                self.bot.send_message(chat_id=self.user_id, text=message)
        else:
            return
