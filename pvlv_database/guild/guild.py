from core.db.query import (pull_data, push_data)
from core.db.modules.class_message import MessagesField


class GuildData(object):

    def __init__(self, guild_id):

        self.scope = 'Telegram'
        self.guild_id = guild_id

        self.table = 'guilds'  # table where the guilds data will be saved

        # guild data logging
        self.guild_name = None
        self.owner_id = None
        self.owner_name = None
        self.bot_paused = False
        self.bot_disabled = False
        self.prefix = '.'
        self.quiet_prefix = ','
        self.sudo_prefix = '#'
        self.languages = ['eng']
        self.modules = {}

        self.pro_guild = 0
        self.deep_logging = False
        self.level_up_notification = True
        self.level_up_destination = 2
        self.start_notifications_at_level = 5
        self.bits_min_add = 0
        self.bits_max_add = 1
        self.use_global_bits = True
        self.member_total = 0

        self.get_data()

    def set_data(self):

        data = {
            'unique_id': self.guild_id,
            'guild_name': self.guild_name,
            'owner_id': self.owner_id,
            'owner_name': self.owner_name,
            'bot_paused': self.bot_paused,
            'bot_disabled': self.bot_disabled,
            'prefix': self.prefix,
            'quiet_prefix': self.quiet_prefix,
            'sudo_prefix': self.sudo_prefix,
            'languages': self.languages,
            'modules': self.modules,

            'pro_guild': self.pro_guild,
            'deep_logging': self.deep_logging,
            'level_up_notification': self.level_up_notification,
            'level_up_destination': self.level_up_destination,
            'start_notifications_at_level': self.start_notifications_at_level,
            'bits_min_add': self.bits_min_add,
            'bits_max_add': self.bits_max_add,
            'use_global_bits': self.use_global_bits,
            'member_total': self.member_total,
        }

        push_data(self.scope, self.table, self.guild_id, data)

    def get_data(self):

        data = pull_data(self.scope, self.table, self.guild_id)

        self.guild_name = data.get('guild_name', self.guild_name)
        self.owner_id = data.get('owner_id', self.owner_id)
        self.owner_name = data.get('owner_name', self.owner_name)
        self.bot_paused = data.get('bot_paused', self.bot_paused)
        self.bot_disabled = data.get('bot_disabled', self.bot_disabled)
        self.prefix = data.get('prefix', self.prefix)
        self.quiet_prefix = data.get('quiet_prefix', self.quiet_prefix)
        self.sudo_prefix = data.get('sudo_prefix', self.sudo_prefix)
        self.languages = data.get('languages', self.languages)
        self.modules = data.get('modules', self.modules)

        self.pro_guild = data.get('pro_guild', self.pro_guild)
        self.deep_logging = data.get('deep_logging', self.deep_logging)
        self.level_up_notification = data.get('level_up_notification', self.level_up_notification)
        self.level_up_destination = data.get('level_up_destination', self.level_up_destination)
        self.start_notifications_at_level = data.get('start_notifications_at_level', self.start_notifications_at_level)
        self.bits_min_add = data.get('bits_min_add', self.bits_min_add)
        self.bits_max_add = data.get('bits_max_add', self.bits_max_add)
        self.use_global_bits = data.get('use_global_bits', self.use_global_bits)
        self.member_total = data.get('member_total', self.member_total)
