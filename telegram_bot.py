import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from core.src.settings import TELEGRAM
# for audio download
from io import BytesIO


class TelegramBot(object):

    def __init__(self, token, starter):

        self.token = token
        self.starter = starter

        bot = telegram.Bot(token=token)
        print(bot.get_me().first_name)

        self.stop_bot = False

        """
        COMMANDS
        help - help message
        man - command manual of all active commands
        data - get stats eng
        dati - ottieni statistiche ita
        speech_to_text - convert audio to text
        """
        self.telegram_command_list = ['help', '/man', '/data', '/dati', '/speech_to_text']

    def voice_handler(self, bot, update):
        message = update.message

        duration = message.voice.duration
        audio_bytes = BytesIO()
        file = bot.getFile(message.voice.file_id)
        raw_file = file.download(out=audio_bytes)

        self.starter.update(TELEGRAM, bot, message)
        self.starter.analyze_vocal_message(raw_file, duration)

    def text_handler(self, bot, update):
        message = update.message
        text = update.message.text

        if text.lower() == ('stopbot' or 'stop bot'):
            if self.stop_bot:
                self.stop_bot = False
                bot.send_message(chat_id=message.chat.id, text='Bot started')
            else:
                self.stop_bot = True
                bot.send_message(chat_id=message.chat.id, text='Bot stopped')

        if self.stop_bot:
            return

        self.starter.update(TELEGRAM, bot, message)
        self.starter.analyze_text_message(text)

    def command_converter(self, bot, update):

        message = update.message
        text = update.message.text

        shortcuts = {
            'speech_to_text': 'state speech_to_text -en'
        }

        if str.startswith(text, '/'):
            text = text[1:]
            p = text.find('@')
            if p is not -1:
                text = text[:p]

            for key in shortcuts.keys():
                if key == text:
                    text = shortcuts.get(key)

            self.starter.update(TELEGRAM, bot, message)
            self.starter.analyze_command_message(text)

    def run(self):
        updater = Updater(self.token)
        dp = updater.dispatcher

        for telegram_command in self.telegram_command_list:
            telegram_command = telegram_command[1:]
            dp.add_handler(CommandHandler(telegram_command, self.command_converter))

        dp.add_handler(MessageHandler(Filters.voice, self.voice_handler))
        dp.add_handler(MessageHandler(Filters.text, self.text_handler))

        updater.start_polling()
        updater.idle()
