import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import sys
from threading import Thread
from core.starter import Starter
from core.src.settings import TELEGRAM
from time import sleep

from io import BytesIO
import speech_recognition as sr
from pydub import AudioSegment


def speech_to_text(file):

    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio_data = r.record(source)  # read the entire audio file
        r.pause_threshold = 4.0

    try:
        text = r.recognize_google(audio_data, language='it-IT')
    except Exception as e:
        print(e)
        return ""

    return text


class TelegramBot(object):

    def __init__(self, token):

        self.token = token

        bot = telegram.Bot(token=token)
        print(bot.get_me().first_name)

    def voice_handler(self, bot, update):
        message = update.message
        audio_bytes = BytesIO()
        file = bot.getFile(message.voice.file_id)
        raw = file.download(out=audio_bytes)
        raw.seek(0)
        ogg_audio = AudioSegment.from_ogg(raw)
        filename = "audio.wav"
        ogg_audio.export(filename, format="wav")
        text = speech_to_text(filename)

        print(text)
        t = 'SPEACH TO TEXT:\n{}'.format(text)
        message.reply_text(text=t, quote=True)
        self.analyze_message(bot, message, text)

    def text_handler(self, bot, update):
        message = update.message
        text = update.message.text
        self.analyze_message(bot, message, text)

    @staticmethod
    def analyze_message(bot, message, text):

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
            'text': text if text is not None else '',
            'message_type': False
        }

        c = Starter(TELEGRAM, bot, message, message_data)
        r = c.analyze_message()
        if r != "" and r is not None:
            bot.send_chat_action(chat_id=message.chat.id, action=telegram.ChatAction.TYPING)
            sleep(len(r) / 16)
            bot.send_message(chat_id=message.chat.id, text=r)

    def run(self):
        updater = Updater(self.token)
        dp = updater.dispatcher

        dp.add_handler(MessageHandler(Filters.voice, self.voice_handler))
        dp.add_handler(MessageHandler(Filters.text, self.text_handler))

        def stop_and_restart():
            """Gracefully stop the Updater and replace the current process with a new one"""
            updater.stop()
            os.execl(sys.executable, sys.executable, *sys.argv)

        def restart(update, context):
            update.message.reply_text('Bot is restarting...')
            Thread(target=stop_and_restart).start()

        dp.add_handler(CommandHandler('r', restart, filters=Filters.user(username='@AbbestiaDC')))

        updater.start_polling()
        updater.idle()
