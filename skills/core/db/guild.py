# modules_data
from .modules_data.log import Log


class GuildData(object):

    def __init__(self, client, scope, guild_id):

        self.client = client
        self.scope = scope
        self.guild_id = guild_id

        self.table = 'guilds_data' # table where the guilds data will be saved
        self.me = 'me'

        # guild data logging
        self.guild_name = None
        self.owner_id = None
        self.owner_name = None
        self.prefix = '.'
        self.quiet_prefix = '.'
        self.sudo_prefix = '#'
        self.languages = ['eng']
        # composed data
        self._class_log = Log()
        self.log = self._class_log
        self.message_reply = {}
        self.bestemmia_reply = {}
        self.badass_character_call = {}
        self.pickup_line_call = {}

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
            'log': self._class_log.build_data(),
            'message_reply': self.message_reply,
            'bestemmia_reply': self.bestemmia_reply,
            'badass_character_call': self.badass_character_call,
            'pickup_line_call': self.pickup_line_call
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
        self.log = self._class_log.extract_data(user_data.get('log'))
        self.message_reply = user_data.get('message_reply')
        self.bestemmia_reply = user_data.get('bestemmia_reply')
        self.badass_character_call = user_data.get('badass_character_call')
        self.pickup_line_call = user_data.get('pickup_line_call')
