from core.src.settings import (
    XP_NEXT_LEVEL, MSG_DISABLED, MSG_DIRECT,
    COMMAND, IMAGE, DOCUMENT, VOICE, VIDEO_NOTE, STICKER,
    SUDO_PREFIX, OVERRIDE_PREFIX)
from pymongo import MongoClient
from .guild import GuildData
from .user import UserData
from .user_new import UserDataNew

from datetime import timedelta


class DB(object):

    def __init__(self, connection_string):

        self.client = MongoClient(connection_string)

        self.guild = None
        self.user = None
        self.user_global = None
        self.user_new = UserDataNew

        self.user_level_up = False
        self.user_global_level_up = False

        self.__scope = None
        self.__iter_collections_iter = None

    def update_data(self, scope, guild_id, user_id):

        self.user_level_up = False
        self.user_global_level_up = False

        try:
            self.guild = GuildData(self.client, scope, guild_id)
            self.user = UserData(self.client, scope, guild_id, user_id)
            self.user_global = UserData(self.client, scope, 'user_data_global', user_id)

            self.user_new = UserDataNew(self.client, guild_id, user_id)

        except Exception as e:
            print('Exception in db update_data: {}'.format(e))

        self.__iter_collections_iter = None

        return

    def set_data(self):

        try:
            self.guild.set_data()
            self.user.set_data()
            self.user_global.set_data()

            self.user_new.set_data()

        except Exception as e:
            print('Exception in db set_data: {}'.format(e))

    @property
    def username(self):
        return self.user.user_name

    @username.setter
    def username(self, value):
        self.user.user_name = value
        self.user_global.user_name = value
        self.user_new.user_name = value

    @property
    def language(self):
        return self.guild.languages[0]

    def iter_guild(self, scope):
        self.__scope = scope
        collections = self.client[scope].collection_names()
        self.__iter_collections_iter = iter(collections)

    def next_guild(self):
        guild_id = next(self.__iter_collections_iter)
        if guild_id is None:
            return None
        try:
            guild_id = int(guild_id)
            self.guild.update_guild_data(self.__scope, guild_id)
        except Exception as e:
            print(e)
            return -1
        return guild_id

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

            xp_value += xp_add
            xp_to_next_level = self.calculate_xp_upto_level(level)
            if xp_to_next_level <= xp_value:
                level += 1
                setattr(self, obj+'_level_up', True)
            if level == self.guild.start_notifications_at_level:
                level_up_notification = True
                xp.level_up_notification = level_up_notification

            xp.xp_value = xp_value
            xp.level = level

    @property
    def xp(self):
        return self.user.xp.xp_value

    @property
    def xp_global(self):
        return self.user_global.xp.xp_value

    @property
    def xp_gained_in_current_level(self):
        return int(self.xp - self.calculate_xp_upto_level(self.level - 1))

    @property
    def xp_gained_in_current_level_global(self):
        return int(self.xp_global - self.calculate_xp_upto_level(self.level_global - 1))

    # the formula to calculate the xp needed to level-up
    @staticmethod
    def calculate_xp_upto_level(level):
        return (level * (level + 1) / 4) * XP_NEXT_LEVEL

    # calculate the xp of the level, how much xp you have to gain to go to the next level
    def get_max_xp_of_level(self, level):
        if level is 0:
            return self.calculate_xp_upto_level(level)
        else:
            prev_level = level - 1
            return self.calculate_xp_upto_level(level) - self.calculate_xp_upto_level(prev_level)

    # the xp that is contained in the given level
    @property
    def level_xp(self):
        return int(self.get_max_xp_of_level(self.level))

    @property
    def level_xp_global(self):
        return int(self.get_max_xp_of_level(self.level_global))

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
    def level_global(self):
        return self.user_global.xp.level

    @property
    def rank(self):
        return self.user.get_user_rank()

    @property
    def rank_global(self):
        return self.user_global.get_user_rank()

    @property
    def ranking(self, **kwargs):
        return self.user.build_ranking(kwargs)

    @property
    def ranking_global(self, **kwargs):
        return self.user_global.build_ranking(kwargs)

    def update_msg(self, time_log, time_spent_to_type):

        for obj in ['user', 'user_global', 'guild']:
            for scope in ['hour', 'day', 'month']:

                msg = getattr(self, obj).msg

                if scope == 'hour':
                    time = time_log.replace(minute=0, second=0, microsecond=0)
                    max_len = 72
                    log_time_by_scope = msg.log_time_by_hour
                    by_scope = msg.by_hour
                    time_spent_by_scope = msg.time_spent_by_hour
                elif scope == 'day':
                    time = time_log.replace(hour=0, minute=0, second=0, microsecond=0)
                    max_len = 90
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
                    log_time_by_scope.append(time)

                if scope == 'hour':
                    sub = time - db_timestamp
                    condition = sub >= timedelta(hours=1)
                elif scope == 'day':
                    sub = time - db_timestamp
                    condition = sub >= timedelta(days=1)
                else:
                    condition = time.month > db_timestamp.month or (time.month == 1 and db_timestamp.month == 12)

                if condition:
                    log_time_by_scope.insert(0, time)
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

    def update_messages_by_type(self, message_type, command_type):
        if message_type is COMMAND:
            if command_type is OVERRIDE_PREFIX:
                self.guild.msg.override += 1
                self.user.msg.override += 1
                self.user_global.msg.override += 1
            elif command_type is SUDO_PREFIX:
                self.guild.msg.sudo += 1
                self.user.msg.sudo += 1
                self.user_global.msg.sudo += 1
            else:
                self.guild.msg.commands += 1
                self.user.msg.commands += 1
                self.user_global.msg.commands += 1
        elif message_type is IMAGE:
            self.guild.msg.img += 1
            self.user.msg.img += 1
            self.user_global.msg.img += 1
        elif message_type is DOCUMENT:
            self.guild.msg.documents += 1
            self.user.msg.documents += 1
            self.user_global.msg.documents += 1
        elif message_type is VOICE:
            self.guild.msg.vocals += 1
            self.user.msg.vocals += 1
            self.user_global.msg.vocals += 1
        elif message_type is VIDEO_NOTE:
            self.guild.msg.video_note += 1
            self.user.msg.video_note += 1
            self.user_global.msg.video_note += 1
        elif message_type is STICKER:
            self.guild.msg.stickers += 1
            self.user.msg.stickers += 1
            self.user_global.msg.stickers += 1
        else:
            return

    def increment_command_interactions(self, command_name, datetime_log):
        self.user.commands.increment_command_interactions(command_name, datetime_log)
        self.user_global.commands.increment_command_interactions(command_name, datetime_log)

    def get_command_interactions(self, command_name):
        return self.user.commands.get_command_interactions(command_name)
