import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from pvlv.static.configurations import TOKEN
from pvlv import TextHandler


# for audio download
from io import BytesIO


"""
COMMANDS FOR TELEGRAM
help - help message
man - command manual of all active commands
data - get user stats
stt - speech to text
level - show your level
ranking - show ranking of the top 10
"""


class TelegramBot(object):

    def __init__(self):

        self.bot = telegram.Bot(token=TOKEN)
        print(self.bot.get_me().first_name)

        self.telegram_command_list = ['/help', '/man', '/data', '/stt', '/pause_bot', '/level', '/ranking']

    @staticmethod
    def voice_handler(update, context):
        message = update.message

        duration = message.voice.duration
        audio_bytes = BytesIO()
        # file = bot.getFile(message.voice.file_id)
        # raw_file = file.download(out=audio_bytes)

    def text_handler(self, update, context):

        username = update.message.from_user.name
        chat_name = update.message.chat.title
        chat_type = update.message.chat.type
        private = True if chat_type == 'private' else False

        th = TextHandler(update, self.bot)
        th.handle(
            update.message.from_user.id,
            update.message.from_user.name,
            update.message.chat.id,
            username if private else chat_name,
            update.message.date,
            update.message.text
        )

    @staticmethod
    def command_converter(update, context):

        message = update.message
        text = update.message.text

        if str.startswith(text, '/'):
            text = text[1:]
            p = text.find('@')
            if p is not -1:
                text = text[:p]

            text = text.replace('_', '.')

    def run(self):
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        for telegram_command in self.telegram_command_list:
            telegram_command = telegram_command[1:]
            dp.add_handler(CommandHandler(telegram_command, self.command_converter))

        dp.add_handler(MessageHandler(Filters.voice, self.voice_handler))
        dp.add_handler(MessageHandler(Filters.text, self.text_handler))

        updater.start_polling()
        updater.idle()
