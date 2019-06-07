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
        self.prefix = '.'
        self.quiet_prefix = ','
        self.sudo_prefix = '#'
        self.languages = ['eng']
        self.modules = {}
        # composed data
        self._class_user_data_log = UserDataLog()
        self.log = self._class_user_data_log

        self.get_guild_data()

    def set_guild_data(self):

        if self.guild_id is None:
            self.guild_id = self.me

        guild_data = {
            '_id': self.guild_id,
            'guild_name': self.guild_name,
            'owner_id': self.owner_id,
            'owner_name': self.owner_name,
            'prefix': self.prefix,
            'quiet_prefix': self.quiet_prefix,
            'sudo_prefix': self.sudo_prefix,
            'languages': self.languages,
            'modules': self.modules,
            'log': self._class_user_data_log.build_data(),
        }

        collection = self.client[self.scope][self.table]
        query = {'_id': self.guild_id}
        cursor = collection.find(query)
        user_data_in_db = None
        for doc in cursor:
            user_data_in_db = doc
        if user_data_in_db is not None:
            guild_data.pop("_id")
            collection.update_one(query, {'$set': guild_data})
        else:
            collection.insert_one(guild_data)

    def get_guild_data(self):

        if self.guild_id is None:
            self.guild_id = self.me

        collection = self.client[self.scope][self.table]
        cursor = collection.find({'_id': self.guild_id})
        user_data = None
        for doc in cursor:
            user_data = doc
        if user_data is None:
            return

        self.guild_name = user_data.get('guild_name')
        self.owner_id = user_data.get('owner_id')
        self.owner_name = user_data.get('owner_name')
        self.prefix = user_data.get('prefix')
        self.quiet_prefix = user_data.get('quiet_prefix')
        self.sudo_prefix = user_data.get('sudo_prefix')
        self.languages = user_data.get('languages')
        self.modules = user_data.get('modules')
        self.log = self._class_user_data_log.extract_data(user_data.get('log', self._class_user_data_log.build_data()))


class UserDataLog(object):

    def __init__(self):

        self.deep_logging = False
        self.level_up_notification = True
        self.level_up_destination = 0
        self.start_notifications_at_level = 5
        self.bits_min_add = 0
        self.bits_max_add = 1
        self.use_global_bits = True
        self.member_total = 0
        self.msg_total = 0
        self.msg_commands = 0
        self.msg_override = 0
        self.msg_sudo = 0
        self.msg_img = 0
        self.msg_links = 0

    def extract_data(self, raw_data):
        self.deep_logging = raw_data.get('deep_logging', self.deep_logging)
        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.level_up_destination = raw_data.get('level_up_destination', self.level_up_destination)
        self.start_notifications_at_level = raw_data.get('start_notifications_at_level', self.start_notifications_at_level)
        self.bits_min_add = raw_data.get('bits_min_add', self.bits_min_add)
        self.bits_max_add = raw_data.get('bits_max_add', self.bits_max_add)
        self.use_global_bits = raw_data.get('use_global_bits', self.use_global_bits)
        self.member_total = raw_data.get('member_total', self.member_total)
        self.msg_total = raw_data.get('msg_total', self.msg_total)
        self.msg_commands = raw_data.get('msg_commands', self.msg_commands)
        self.msg_override = raw_data.get('msg_override', self.msg_override)
        self.msg_sudo = raw_data.get('msg_sudo', self.msg_sudo)
        self.msg_img = raw_data.get('msg_img', self.msg_img)
        self.msg_links = raw_data.get('msg_links', self.msg_links)

        return self

    def build_data(self):

        data_out = {
            'deep_logging': self.deep_logging,
            'level_up_notification': self.level_up_notification,
            'level_up_destination': self.level_up_destination,
            'start_notifications_at_level': self.start_notifications_at_level,
            'bits_min_add': self.bits_min_add,
            'bits_max_add': self.bits_max_add,
            'use_global_bits': self.use_global_bits,
            'member_total': self.member_total,
            'msg_total': self.msg_total,
            'msg_commands': self.msg_commands,
            'msg_override': self.msg_override,
            'msg_sudo': self.msg_sudo,
            'msg_img': self.msg_img,
            'msg_links': self.msg_links,
        }

        return data_out
