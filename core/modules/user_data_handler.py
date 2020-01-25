from core.src.settings import *
from core.modules.user_log.user_data_top_level_log import UserDataTopLevelLog
from core.modules.user_log.user_data_deep_log import UserDataDeepLog
import math
from datetime import datetime


class UserData(object):

    def __init__(self, bot, database, language, text, message_type, prefix_type, deep_logging, time_spent_extra=0):

        self.bot = bot
        self.database = database
        self.language = language
        self.text = text
        self.text_len = len(text)
        self.message_type = message_type
        self.prefix_type = prefix_type
        self.time_spent_extra = time_spent_extra
        self.deep_logging = deep_logging

    def log_data(self):

        now = datetime.utcnow()

        user_data_top_level_log = UserDataTopLevelLog(
            self.bot,
            self.database,
            self.text_len,
            self.language
        )
        user_data_top_level_log.log_data()

        if self.deep_logging:
            if self.message_type is TEXT:
                time_spent = math.ceil(self.text_len * TIME_SAMPLE_VALUE / SAMPLE_STRING_LEN)
                time_spent += self.time_spent_extra
            else:
                time_spent = self.time_spent_extra
            user_data_deep_log = UserDataDeepLog(
                self.bot,
                self.database,
                self.text_len,
                time_spent,
                now,
                self.message_type,
                self.prefix_type
            )
            user_data_deep_log.log_data()

        self.database.set_data()
