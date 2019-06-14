from core.src.settings import XP_NEXT_LEVEL, MSG_DISABLED, MSG_DIRECT
from pymongo import MongoClient
from .guild import GuildData
from .user import UserData

from datetime import timedelta


class DB(object):

    def __init__(self, connection_string):

        self.client = MongoClient(connection_string)

        self.guild = None
        self.user = None
        self.user_global = None

        self.user_level_up = False
        self.user_global_level_up = False

    def update_data(self, scope, guild_id, user_id):

        self.user_level_up = False
        self.user_global_level_up = False

        self.guild = GuildData(self.client, scope, guild_id)
        self.user = UserData(self.client, scope, guild_id, user_id)
        self.user_global = UserData(self.client, scope, 'user_data_global', user_id)

        return

    def set_data(self):
        self.guild.set_guild_data()
        self.user.set_user_data()
        self.user_global.set_user_data()
        return

    @property
    def user_name(self):
        return self.user.user_name

    @user_name.setter
    def user_name(self, value):
        self.user.user_name = value
        self.user_global.user_name = value

    def update_bits(self, bits_add):

        for obj in ['user', 'user_global']:
            bill = getattr(self, obj).bill
            bits = bill.bits

            bits += bits_add

            bill.bits = bits

    def update_xp(self, xp_add):

        for obj in ['user', 'user_global']:
            xp = getattr(self, obj).xp
            xp_value = xp.xp_value
            level = int(xp.level)
            level_up_notification = xp.level_up_notification

            xp_value += xp_add
            xp_to_next_level = XP_NEXT_LEVEL*level*1.2
            if xp_to_next_level <= xp_value:
                level += 1
                setattr(self, obj+'_level_up', True)
            if level == self.guild.start_notifications_at_level:
                level_up_notification = True
                xp.level_up_notification = level_up_notification

            xp.xp_value = xp_value
            xp.level = level

    def is_user_level_up(self):
        return self.user_level_up

    def user_level_up_destination(self):

        if self.guild.level_up_notification and self.user.xp.level_up_notification:
            return self.guild.level_up_destination
        else:
            return MSG_DISABLED

    @property
    def level(self):
        return self.user.xp.level

    def is_user_global_level_up(self):
        return self.user_global_level_up

    def user_global_level_up_destination(self):

        if self.user_global.xp.level_up_notification:
            return MSG_DIRECT
        else:
            return MSG_DISABLED

    @property
    def global_level(self):
        return self.user_global.xp.level

    def update_msg(self, time_log, time_spent_to_type):

        for obj in ['user', 'user_global', 'guild']:
            for scope in ['hour', 'day', 'month']:

                msg = getattr(self, obj).msg

                if scope == 'hour':
                    time = time_log.replace(minute=0, second=0, microsecond=0)
                    max_len = 24
                    log_time_by_scope = msg.log_time_by_hour
                    by_scope = msg.by_hour
                    time_spent_by_scope = msg.time_spent_by_hour
                elif scope == 'day':
                    time = time_log.replace(hour=0, minute=0, second=0, microsecond=0)
                    max_len = 31
                    log_time_by_scope = msg.log_time_by_day
                    by_scope = msg.by_day
                    time_spent_by_scope = msg.time_spent_by_day
                elif scope == 'month':
                    time = time_log
                    max_len = 120
                    log_time_by_scope = msg.log_time_by_month
                    by_scope = msg.by_month
                    time_spent_by_scope = msg.time_spent_by_month
                else:
                    return

                try:
                    db_timestamp = log_time_by_scope[0]
                    if len(log_time_by_scope) > max_len:
                        log_time_by_scope.pop()
                    if len(by_scope) > max_len:
                        by_scope.pop()
                    if len(time_spent_by_scope) > max_len:
                        time_spent_by_scope.pop()
                except IndexError:
                    db_timestamp = time
                    log_time_by_scope.append(time_log)

                if scope == 'hour':
                    sub = time_log - db_timestamp
                    condition = sub >= timedelta(hours=1)
                elif scope == 'day':
                    sub = time_log - db_timestamp
                    condition = sub >= timedelta(days=1)
                else:
                    condition = time.month > db_timestamp.month or (time.month == 1 and db_timestamp.month == 12)

                if condition:
                    log_time_by_scope.insert(0,  time_log)
                    by_scope.insert(0, 1)
                    time_spent_by_scope.insert(0, time_spent_to_type)
                else:
                    try:
                        by_scope[0] += 1
                    except IndexError:
                        by_scope.append(1)
                    try:
                        time_spent_by_scope[0] += time_spent_to_type
                    except IndexError:
                        time_spent_by_scope.append(time_spent_to_type)

                if scope == 'hour':
                    msg.log_time_by_hour = log_time_by_scope
                    msg.by_hour = by_scope
                    msg.time_spent_by_hour = time_spent_by_scope
                elif scope == 'day':
                    msg.log_time_by_day = log_time_by_scope
                    msg.by_day = by_scope
                    msg.time_spent_by_day = time_spent_by_scope
                elif scope == 'month':
                    msg.log_time_by_month = log_time_by_scope
                    msg.by_month = by_scope
                    msg.time_spent_by_month = time_spent_by_scope
