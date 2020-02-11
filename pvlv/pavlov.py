import telegram
from telegram.ext import Updater, MessageHandler, Filters

from static.configurations import TOKEN
from handlers.text_handler import TextHandler
from handlers.img_handler import ImgHandler
from handlers.vocal_handler import VocalHandler
from debug.execution_time import ExecutionTime


class TelegramBot(ExecutionTime):

    def __init__(self):
        super().__init__()

        self.bot = telegram.Bot(token=TOKEN)
        print(self.bot.get_me().first_name)

    def vocal_handler(self, update, context):
        self.start_time_calculation('vocal_all')
        th = VocalHandler(update, self.bot)
        th.handle()
        self.stop_time_calculation('vocal_all', message='All vocal handler')

    def img_handler(self, update, context):
        self.start_time_calculation('img_all')
        th = ImgHandler(update, self.bot)
        th.handle()
        self.stop_time_calculation('img_all', message='All img handler')

    def text_handler(self, update, context):
        self.start_time_calculation('text_all')
        th = TextHandler(update, self.bot)
        th.handle()
        self.stop_time_calculation('text_all', message='All text handler')

    def run(self):
        updater = Updater(TOKEN, use_context=True)
        dp = updater.dispatcher

        dp.add_handler(MessageHandler(Filters.voice, self.vocal_handler))
        dp.add_handler(MessageHandler(Filters.text, self.text_handler))
        dp.add_handler(MessageHandler(Filters.photo, self.img_handler))

        updater.start_polling()
        updater.idle()
