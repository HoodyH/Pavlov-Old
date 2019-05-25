from pymongo import MongoClient
from skills.core.utils.data_models import *


class MongoDB(object):

    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)

    # with the data config needed
    def create_guild(self, guild_id, guild_name):

        print(self.client.telegram.list_collection_names())
        collection = self.client.telegram.config

        collection.insert_one(CONFIG_MODEL).inserted_id

        return

    def create_user(self):
        return

    def create_command(self):
        return

    def create_new_response(self):
        return
