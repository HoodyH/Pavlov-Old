import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import sys
from threading import Thread
from core.starter import Starter
from core.src.settings import TELEGRAM

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

        self.stop_bot = False
        self.speech_to_text = False

        """
        COMMANDS
        data - get stats eng
        dati - ottieni statistiche ita
        """
        self.telegram_command_list = ['/data', '/dati']

    def voice_handler(self, bot, update):

        if self.stop_bot:
            return

        if self.speech_to_text:
            return

        message = update.message
        audio_bytes = BytesIO()
        file = bot.getFile(message.voice.file_id)
        raw = file.download(out=audio_bytes)
        raw.seek(0)
        ogg_audio = AudioSegment.from_ogg(raw)
        filename = "audio.wav"
        ogg_audio.export(filename, format="wav")
        text = speech_to_text(filename)

        t = 'SPEECH TO TEXT:\n{}'.format(text)
        message.reply_text(text=t, quote=True)
        self.analyze_message(bot, message, text)

    def text_handler(self, bot, update):
        message = update.message
        text = update.message.text

        if text.lower() == 'converti audio':
            if self.speech_to_text:
                self.speech_to_text = False
                bot.send_message(chat_id=message.chat.id, text='Speech to text on')
            else:
                self.speech_to_text = True
                bot.send_message(chat_id=message.chat.id, text='Speech to text off')

        if text.lower() == ('stopbot' or 'stop bot'):
            if self.stop_bot:
                self.stop_bot = False
                bot.send_message(chat_id=message.chat.id, text='Bot started')
            else:
                self.stop_bot = True
                bot.send_message(chat_id=message.chat.id, text='Bot stopped')

        if self.stop_bot:
            return

        self.analyze_message(bot, message, text)

    def command_converter(self, bot, update):
        message = update.message
        text = update.message.text

        if str.startswith(text, '/'):
            temp = list(text)
            temp[0] = '.'
            text = ''.join(temp)
            p = text.find('@')
            if p is not -1:
                text = text[:p]
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
            # bot.send_chat_action(chat_id=message.chat.id, action=telegram.ChatAction.TYPING)
            # sleep(len(r) / 16)
            bot.send_message(chat_id=message.chat.id, text=r)

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
