from pvlv_database.user.user import User


class Database(object):

    def __init__(self, connection):
        self.connection = connection
