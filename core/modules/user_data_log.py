from core.src.settings import *
from core.src.static_modules import db
from core.src.utils.message_sender import MessageSender
from datetime import datetime
import math


class UserDataLog(object):

    def __init__(self, scope, bot, guild_id, user_id, language, username, text, prefix_type):

        self.scope = scope
        self.bot = bot
        self.guild_id = guild_id
        self.user_id = user_id
        self.language = language
        self.username = username
        self.text = text
        self.text_len = len(text)
        self.prefix_mode = prefix_type

        self.out = None

    def __send_level_up_message(self, level, destination):

        if self.language == ITA:
            message = 'Grande {}\nHai raggiunto il livello {}'.format(self.username, level)
        else:
            message = 'Cool {}\nYou\'ve gain to level {}'.format(self.username, level)

        ms = MessageSender(self.scope, self.bot, self.guild_id, self.user_id, self.guild_id)
        ms.send_message(message, destination)

    def log_data(self):

        db.user_name = self.username

        now = datetime.utcnow()

        time_spent_to_type = math.ceil(self.text_len * TIME_SAMPLE_VALUE / SAMPLE_STRING_LEN)
        db.update_msg(now, time_spent_to_type)

        xp_by_string_len = int(math.ceil(self.text_len * XP_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        xp_add = xp_by_string_len if xp_by_string_len <= XP_MAX_VALUE else XP_MAX_VALUE
        db.update_xp(xp_add)

        if db.is_user_level_up():
            destination = db.user_level_up_destination()
            if destination != MSG_DISABLED:
                self.__send_level_up_message(db.level, destination)

        if db.is_user_global_level_up():
            destination = db.user_global_level_up_destination()
            if destination != MSG_DISABLED:
                self.__send_level_up_message(db.global_level, destination)

        bits_by_string_len = int(math.ceil(self.text_len * BITS_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        bits_add = bits_by_string_len if bits_by_string_len <= BITS_MAX_VALUE else BITS_MAX_VALUE
        db.update_bits(bits_add)

        db.set_data()
