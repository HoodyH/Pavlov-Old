from core.src.settings import *
from random import random
from datetime import datetime, timedelta
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

    def _xp_manage(self):
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

        # data only for directs
        bits_min_add = 0
        bits_max_add = 4
        # local guild bits generation
        bits_add = int(random() * (db.guild.log.bits_max_add - db.guild.log.bits_min_add) + db.guild.log.bits_min_add)
        db.user.bits += bits_add
        # global bits generation
        bits_add = int(random() * (bits_max_add - bits_min_add) + bits_min_add)
        db.user_global.bits += bits_add

    def log_data(self):

        db.user.user_name = self.user_name

        now = datetime.utcnow()
        msg_counter = 1
        time_spent_to_type = int(self.text_len * SAMPLE_TIME_FOR_STRING / SAMPLE_STRING_LEN)

        """
        TIME SPENT BY HOUR
        """
        _now = now.replace(minute=0, second=0, microsecond=0)
        try:
            db_timestamp = db.user.msg.log_time_by_hour[0]
        except IndexError:
            db_timestamp = _now
            db.user.msg.log_time_by_hour.append(_now)

        sub = _now - db_timestamp
        if sub > timedelta(hours=1):
            db.user.msg.log_time_by_hour.insert(0, _now)
            db.user.msg.by_day.insert(0, 1)
            db.user.msg.time_spent_by_hour.insert(0, time_spent_to_type)
        else:
            try:
                db.user.msg.by_day[0] += msg_counter
            except IndexError:
                db.user.msg.by_day.append(1)

            try:
                db.user.msg.time_spent_by_hour[0] += time_spent_to_type
            except IndexError:
                db.user.msg.time_spent_by_hour.append(time_spent_to_type)

        """
        TIME SPENT BY DAY
        """
        _now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        try:
            db_timestamp = db.user.msg.log_time_by_day[0]
        except IndexError:
            db_timestamp = _now
            db.user.msg.log_time_by_day.append(_now)

        sub = _now - db_timestamp
        if sub > timedelta(days=1):
            db.user.msg.log_time_by_day.insert(0, _now)
            db.user.msg.by_day.insert(0, 1)
            db.user.msg.time_spent_by_day.insert(0, time_spent_to_type)
        else:
            try:
                db.user.msg.by_day[0] += msg_counter
            except IndexError:
                db.user.msg.by_day.append(1)

            try:
                db.user.msg.time_spent_by_day[0] += time_spent_to_type
            except IndexError:
                db.user.msg.time_spent_by_day.append(time_spent_to_type)

        """
        TIME SPENT BY MONTH
        """
        _now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        try:
            db_timestamp = db.user.msg.log_time_by_month[0]
        except IndexError:
            db_timestamp = _now
            db.user.msg.log_time_by_month.append(_now)

        if _now.month > db_timestamp.month or (_now.month == 1 and db_timestamp.month == 12):
            db.user.msg.log_time_by_month.insert(0, _now)
            db.user.msg.by_day.insert(0, 1)
            db.user.msg.time_spent_by_month.insert(0, time_spent_to_type)
        else:
            try:
                db.user.msg.by_day[0] += msg_counter
            except IndexError:
                db.user.msg.by_day.append(1)

            try:
                db.user.msg.time_spent_by_month[0] += time_spent_to_type
            except IndexError:
                db.user.msg.time_spent_by_month.append(time_spent_to_type)

        if db.user.deep_logging and db.guild.log.deep_logging:
            if self.prefix_mode is COMMAND_PREFIX:
                db.user.msg.commands += 1
                db.guild.log.msg.commands += 1
            elif self.prefix_mode is OVERRIDE_PREFIX:
                db.user.msg.override += 1
                db.guild.log.msg.override += 1
            elif self.prefix_mode is SUDO_PREFIX:
                db.user.msg.sudo += 1
                db.guild.log.msg_sudo += 1

        db.set_data()
