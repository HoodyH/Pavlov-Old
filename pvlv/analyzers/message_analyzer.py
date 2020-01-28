import math
from pvlv import Database
from pvlv.settings import *


class MessageAnalyzer(object):
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__text = ''
        self.__message_type = None

    def message_text(self, text):
        self.__text = text

    def message_type(self, message_type):
        self.__message_type = message_type

    def analyze(self):

        now = datetime.utcnow()

        text_len = len(self.__text)

        xp_uncut = int(math.ceil(text_len * XP_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        xp = xp_uncut if xp_uncut <= XP_MAX_VALUE else XP_MAX_VALUE
        self.database.update_xp(xp_uncut)

        if self.database.is_user_level_up():
            destination = self.database.user_level_up_destination()
            if destination != MSG_DISABLED:
                self.__send_level_up_message(self.database.level, destination)


        bits_by_string_len = int(math.ceil(self.text_len * BITS_SAMPLE_VALUE / SAMPLE_STRING_LEN))
        bits_add = bits_by_string_len if bits_by_string_len <= BITS_MAX_VALUE else BITS_MAX_VALUE
        self.database.update_bits(bits_add)