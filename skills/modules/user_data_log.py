from skills.core.settings import *
from random import random


class UserDataLog(object):

    def __init__(self, scope, guild_id, user_id, user_name, text, prefix_type):

        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id
        self.user_name = user_name
        self.text = text
        self.prefix_mode = prefix_type

        self.out = None

    def log_data(self):

        # global data for all guilds
        xp_min_add = 10
        xp_max_add = 25
        level_increment_value = 200
        time_per_message = 6

        # data only for directs
        start_notifications_at_level = 3
        bits_min_add = 0
        bits_max_add = 4

        db.user.user_name = db.user_global.user_name = self.user_name

        # messages sent
        db.user.msg_total += 1
        db.user_global.msg_total += 1
        db.guild.log.msg_total += 1

        if db.user.deep_logging:
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

        xp_add = int(random() * (xp_max_add - xp_min_add) + xp_min_add)

        # guild level manage
        db.user.xp += xp_add
        local_next_level = db.user.level * level_increment_value
        if local_next_level <= db.user.xp:
            db.user.level += 1

            if db.user.level == db.guild.log.start_notifications_at_level:
                db.user.level_up_notification = True

            if db.user.level_up_notification:
                # send message (private or in the group) based on config file
                self.out = "levelup"

        # global level manage
        db.user_global.xp += xp_add
        local_next_level = db.user_global.level * level_increment_value
        if local_next_level <= db.user_global.xp:
            db.user_global.level += 1

            if db.user_global.level == start_notifications_at_level:
                db.user_global.level_up_notification = True

            if db.user_global.level_up_notification:
                # send message (private or in the group) based on config file
                self.out = "levelup"



        # time spent
        db.user.time_spent_sec += time_per_message
        db.user_global.time_spent_sec += time_per_message

        # local guild bits generation
        bits_add = int(random() * (db.guild.log.bits_max_add - db.guild.log.bits_min_add) + db.guild.log.bits_min_add)
        db.user.bits += bits_add
        # global bits generation
        bits_add = int(random() * (bits_max_add - bits_min_add) + bits_min_add)
        db.user_global.bits += bits_add

        db.set_data()

        return
