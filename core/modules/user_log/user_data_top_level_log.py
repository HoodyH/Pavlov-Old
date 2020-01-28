from pvlv.settings import *
from pvlv_image_builder.draw_levels import DrawLevelUp
from core.src.text_reply.reply_modules.level_reply import (
    user_field, text_description
)
import math


class UserDataTopLevelLog(object):

    def __init__(self, bot, database, text_len, language):
        self.bot = bot
        self.database = database
        self.text_len = text_len
        self.language = language

    def __send_level_up_message(self, level, destination):

        data = {
            'level': level,
            'title': user_field(self.language, self.bot.user.username),
            'text': text_description(self.language, level),
        }

        dl = DrawLevelUp(data)
        dl.draw_level_up()

        self.bot.send_image(dl.get_image(), destination)

    def log_data(self):

        xp_by_string_len = int(math.ceil(self.text_len * XP_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        xp_add = xp_by_string_len if xp_by_string_len <= XP_MAX_VALUE else XP_MAX_VALUE
        self.database.update_xp(xp_add)

        if self.database.is_user_level_up():
            destination = self.database.user_level_up_destination()
            if destination != MSG_DISABLED:
                self.__send_level_up_message(self.database.level, destination)

        if self.database.is_user_global_level_up():
            destination = self.database.user_global_level_up_destination()
            if destination != MSG_DISABLED:
                self.__send_level_up_message(self.database.level_global, destination)

        bits_by_string_len = int(math.ceil(self.text_len * BITS_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        bits_add = bits_by_string_len if bits_by_string_len <= BITS_MAX_VALUE else BITS_MAX_VALUE
        self.database.update_bits(bits_add)
