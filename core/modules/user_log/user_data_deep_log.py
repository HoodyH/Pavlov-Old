
class UserDataDeepLog(object):

    def __init__(self, bot, database, text_len, time_spent, datetime_message, message_type, prefix_type):

        self.bot = bot
        self.database = database
        self.text_len = text_len
        self.time_spent = time_spent
        self.datetime_message = datetime_message
        self.message_type = message_type
        self.prefix_type = prefix_type

    def log_data(self):

        self.database.username = self.bot.user.username if self.bot.user.username else 'Anonymous'
        self.database.update_msg(self.datetime_message, self.time_spent)
        self.database.update_messages_by_type(self.message_type, self.prefix_type)
