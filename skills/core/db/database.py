from pymongo import MongoClient
from .guild import GuildData
from .user import UserData
from .user_global import UserDataGlobal


class DB(object):

    def __init__(self, connection_string):

        self.client = MongoClient(connection_string)

        self.guild = None
        self.user = None
        self.user_global = None

    def update_data(self, scope, guild_id, user_id):
        self.guild = GuildData(self.client, scope, guild_id)
        self.user = UserData(self.client, scope, guild_id, user_id)
        self.user_global = UserDataGlobal(self.client, scope, guild_id, user_id)
        return

    def set_data(self):
        self.guild.set_guild_data()
        self.user.set_user_data()
        self.user_global.set_user_data()
        return



