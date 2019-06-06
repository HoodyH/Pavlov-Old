from core.src.settings import *
from random import random
import math


class UserDataLog(object):

    def __init__(self, scope, guild_id, user_id, user_name, text, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.user_name = user_name
        self.text = text
        self.text_len = len(text)
        self.prefix_mode = prefix_type

        self.level_increment_value = 500

        self.out = None

    def _guild_level_up(self):
        local_next_level = db.user.level * self.level_increment_value
        if local_next_level <= db.user.xp:
            db.user.level += 1

            if db.user.level == db.guild.log.start_notifications_at_level:
                db.user.level_up_notification = True

            if db.user.level_up_notification:
                # send message (private or in the group) based on config file
                self.out = "Complimenti {} hai raggiunto il livello {}".format(self.user_name, db.user.level)

    def _global_level_up(self):
        local_next_level = db.user_global.level * self.level_increment_value
        if local_next_level <= db.user_global.xp:
            db.user_global.level += 1

    def log_data(self):
        # data only for directs
        bits_min_add = 0
        bits_max_add = 4

        db.user.user_name = db.user_global.user_name = self.user_name

        # messages sent
        db.user.msg_total += 1
        db.user_global.msg_total += 1
        db.guild.log.msg_total += 1

        if db.user.deep_logging and db.guild.log.deep_logging:
            if self.prefix_mode is COMMAND_PREFIX:
                db.user.msg_commands += 1
                db.user_global.msg_commands += 1
                db.guild.log.msg_commands += 1
            elif self.prefix_mode is OVERRIDE_PREFIX:
                db.user.msg_override += 1
                db.user_global.msg_override += 1
                db.guild.log.msg_override += 1
            elif self.prefix_mode is SUDO_PREFIX:
                db.user.msg_sudo += 1
                db.user_global.msg_sudo += 1
                db.guild.log.msg_sudo += 1

        # XP
        # for a string of 30 char, you will gain 10 xp
        xp_str_len_sample = 30
        xp_by_sample = 5
        xp_max = 30
        # do the proportion
        xp_by_string_len = int(math.ceil(self.text_len * xp_by_sample / xp_str_len_sample))
        xp_add = xp_by_string_len if xp_by_string_len <= xp_max else xp_max
        db.user.xp += xp_add
        self._guild_level_up()
        db.user_global.xp += xp_add
        self._global_level_up()

        # TIME SPENT
        # for a string of 30 char, you will stay 9 sec to write it
        time_str_len_sample = 30
        time_sample = 9
        # do the proportion
        time_to_type = int(self.text_len * time_sample / time_str_len_sample)

        db.user.time_spent_sec += time_to_type
        db.user_global.time_spent_sec += time_to_type

        # local guild bits generation
        bits_add = int(random() * (db.guild.log.bits_max_add - db.guild.log.bits_min_add) + db.guild.log.bits_min_add)
        db.user.bits += bits_add
        # global bits generation
        bits_add = int(random() * (bits_max_add - bits_min_add) + bits_min_add)
        db.user_global.bits += bits_add

        db.set_data()

        return
