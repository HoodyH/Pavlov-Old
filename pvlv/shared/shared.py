from pvlv_database.database import Database


global db


def init_database_handler(connection_string):
    global db
    db = Database(connection_string)
