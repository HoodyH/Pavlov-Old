from core.db.query import (pull_data, push_data)
from core.db.modules.class_message import MessagesField


class GuildData(object):

    def __init__(self, client, scope, guild_id):

        self.client = client
        self.scope = scope
        self.guild_id = guild_id

        self.table = 'guilds_data'  # table where the guilds data will be saved
        self.me = 'me'

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

        # composed data
        self._class_msg = MessagesField()
        self.msg = self._class_msg

        self.get_data()

    def set_data(self):

        if self.guild_id is None:
            self.guild_id = self.me

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

            'msg': self._class_msg.build_data(),
        }

        push_data(self.client, self.scope, self.table, self.guild_id, data)

    def get_data(self):

        if self.guild_id is None:
            self.guild_id = self.me

        data = pull_data(self.client, self.scope, self.table, self.guild_id)

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

        self.msg = self._class_msg.extract_data(data.get('msg', self._class_msg.build_data()))

    def update_guild_data(self, scope, guild_id):
        self.scope = scope
        self.guild_id = guild_id
        self.get_data()

    # guild_name
    @property
    def guild_name(self):
        return self.__guild_name

    @guild_name.setter
    def guild_name(self, value):
        self.__guild_name = value

    # owner_id
    @property
    def owner_id(self):
        return self.__owner_id

    @owner_id.setter
    def owner_id(self, value):
        self.__owner_id = value

    # owner_name
    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, value):
        self.__owner_name = value

    # bot_paused
    @property
    def bot_paused(self):
        return self.__bot_paused

    @bot_paused.setter
    def bot_paused(self, value):
        self.__bot_paused = value

    # bot_disabled
    @property
    def bot_disabled(self):
        return self.__bot_disabled

    @bot_disabled.setter
    def bot_disabled(self, value):
        self.__bot_disabled = value

    # prefix
    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, value):
        self.__prefix = value

    # quiet_prefix
    @property
    def quiet_prefix(self):
        return self.__quiet_prefix

    @quiet_prefix.setter
    def quiet_prefix(self, value):
        self.__quiet_prefix = value

    # sudo_prefix
    @property
    def sudo_prefix(self):
        return self.__sudo_prefix

    @sudo_prefix.setter
    def sudo_prefix(self, value):
        self.__sudo_prefix = value

    # languages
    @property
    def languages(self):
        return self.__languages

    @languages.setter
    def languages(self, value):
        self.__languages = value

    # modules
    @property
    def modules(self):
        return self.__modules

    @modules.setter
    def modules(self, value):
        self.__modules = value

    # pro_guild
    @property
    def pro_guild(self):
        return self.__pro_guild

    @pro_guild.setter
    def pro_guild(self, value):
        self.__pro_guild = value

    # deep_logging
    @property
    def deep_logging(self):
        return self.__deep_logging

    @deep_logging.setter
    def deep_logging(self, value):
        self.__deep_logging = value

    # level_up_notification
    @property
    def level_up_notification(self):
        return self.__level_up_notification

    @level_up_notification.setter
    def level_up_notification(self, value):
        self.__level_up_notification = value

    # level_up_destination
    @property
    def level_up_destination(self):
        return self.__level_up_destination

    @level_up_destination.setter
    def level_up_destination(self, value):
        self.__level_up_destination = value

    # start_notifications_at_level
    @property
    def start_notifications_at_level(self):
        return self.__start_notifications_at_level

    @start_notifications_at_level.setter
    def start_notifications_at_level(self, value):
        self.__start_notifications_at_level = value

    # bits_min_add
    @property
    def bits_min_add(self):
        return self.__bits_min_add

    @bits_min_add.setter
    def bits_min_add(self, value):
        self.__bits_min_add = value

    # bits_max_add
    @property
    def bits_max_add(self):
        return self.__bits_max_add

    @bits_max_add.setter
    def bits_max_add(self, value):
        self.__bits_max_add = value

    # use_global_bits
    @property
    def use_global_bits(self):
        return self.__use_global_bits

    @use_global_bits.setter
    def use_global_bits(self, value):
        self.__use_global_bits = value

    # member_total
    @property
    def member_total(self):
        return self.__member_total

    @member_total.setter
    def member_total(self, value):
        self.__member_total = value

    # msg
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value
