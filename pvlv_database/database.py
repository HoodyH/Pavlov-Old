from pvlv_database.user.user import User


class Database(object):

    def __init__(self, guild_id, user_id):

        self.user = User(guild_id, user_id)

    def set_data(self):
        self.user.set_data()
