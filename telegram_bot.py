import telegram
from core.starter import Starter
from core.src.settings import TELEGRAM


class TelegramBot(object):

    def __init__(self, token):

        self.bot = telegram.Bot(token=token)
        self.update_id = None

    def do_stuffs(self, message):

        message_data = {
            'message_id': message.message_id,
            'date': message.date,
            'guild_id': message.chat.id if message.chat.id != message.from_user.id else None,
            'guild_name': message.chat.title if message.chat.title is not None else None,
            'chat': {
                'id': message.chat.id,
                'title': message.chat.title if message.chat.title is not None else None
            },
            'user': {
                'id': message.from_user.id,
                'username': message.from_user.username,
                'is_bot': message.from_user.is_bot,
                'language_code': message.from_user.language_code
                },
            'text': message.text if message.text != '' else None,
            'message_type': False
        }

        c = Starter(TELEGRAM, self.bot, message, message_data)
        return c.analyze_message()

    def run(self):
        """Run the bot."""
        print(self.bot.get_me().first_name)

        while True:
            updates = self.bot.get_updates(offset=self.update_id)
            for u in updates:
                self.update_id = u.update_id + 1
                try:
                    r = self.do_stuffs(u.message)
                    if r is not None:
                        self.bot.send_message(chat_id=u.message.chat.id, text=r)
                except Exception as e:
                    pass
