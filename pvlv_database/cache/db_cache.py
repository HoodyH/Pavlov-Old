from pymongo import MongoClient
from pvlv_database.user.user import User


class DatabaseCache(object):
    """
    cache system to avoid to much calls to the database
    """

    def __init__(self, connection_string):
        self.__connection = MongoClient(connection_string)
        self.__user_cache = []

    def user(self, guild_id, user_id):
        u: User  # define
        for user in self.__user_cache:
            u = user
            if u.user_id == user_id:
                u.guild(guild_id)
                return u

        return User(guild_id, user_id)

    def set_data(self):
        for user in self.__user_cache:
            user.set_data()
