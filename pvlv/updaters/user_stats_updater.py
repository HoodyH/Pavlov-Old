import math
from pvlv import Database
from pvlv.static.types import MessageType
from pvlv.settings import *
from datetime import datetime


class UserStatsUpdater(object):
    def __init__(self, guild_id, user_id):

        self.__guild_id = guild_id
        self.__user_id = user_id
        self.db = Database(self.__guild_id, self.__user_id)

        self.__text = None
        self.__message_type = None
        self.__timestamp = None

    def time_stamp(self, timestamp: datetime):
        self.__timestamp = timestamp

    def message_text(self, text: str):
        self.__text = text

    def message_type(self, message_type: MessageType):
        self.__message_type = message_type

    def analyze(self):

        text_len = len(self.__text)
        time_spent = math.ceil(text_len * TIME_SAMPLE_VALUE / SAMPLE_STRING_LEN)

        if self.__text:
            """
            If is text
            Update time spent for messages
            """
            self.db.user.guild.msg.msg_log.update_log_by_hour((self.__timestamp, 1, time_spent))
            self.db.user.guild.msg.msg_log.update_log_by_day((self.__timestamp, 1, time_spent))
            self.db.user.guild.msg.msg_log.update_log_by_month((self.__timestamp, 1, time_spent))
            """
            Update XP
            """
            xp_uncut = int(math.ceil(text_len * XP_SAMPLE_VALUE / SAMPLE_STRING_LEN))
            xp = xp_uncut if xp_uncut <= XP_MAX_VALUE else XP_MAX_VALUE
            self.db.user.guild.xp.xp_value += xp
            """
            Update Bill
            """
            bits_uncut = int(math.ceil(text_len * BITS_SAMPLE_VALUE / SAMPLE_STRING_LEN))
            bits = bits_uncut if bits_uncut <= BITS_MAX_VALUE else BITS_MAX_VALUE
            self.db.user.guild.bill.bits += bits

        if self.__message_type is MessageType.IMAGE:
            """
            Update Parameters Based on a default time to send a picture
            """
            self.db.user.guild.msg.img_log.update_log_by_hour((self.__timestamp, 1, 6))
            self.db.user.guild.msg.img_log.update_log_by_day((self.__timestamp, 1, 6))
            self.db.user.guild.msg.img_log.update_log_by_month((self.__timestamp, 1, 6))

            self.db.user.guild.xp.xp_value += 5
            self.db.user.guild.bill.bits += 1

        self.db.set_data()

    def is_level_up(self):
        if self.db.user.guild.xp.is_level_up:
            pass
