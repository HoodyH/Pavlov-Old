class UserData(object):

    def __init__(self, client, scope, guild_id, user_id):

        self.client = client
        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id

        directs = "bot_directs"
        self.table = str(guild_id) if guild_id is not None else directs

        # user data logging
        self.user_name = None
        self.time_zone = 0
        self.deep_logging = True
        self._class_msg = MessagesCounters()
        self.msg = self._class_msg
        self.xp = 0
        self.level_up_notification = False
        self.level = 0
        self.role = 0
        self.bits = 10
        self.swear_words_counter = 0
        self.swear_words_xp = 0
        self.swear_words = {}
        self.toxicity_rank = 0
        self.soft_warnings = 0
        self.hard_warnings = 0
        self.admin_warnings = 0
        self.gender = None
        self.age = None
        self.country = None
        self.speak_in_vc = None

        self.get_user_data()

    def set_user_data(self):

        user_data = {
            '_id': self.user_id,
            'user_name': self.user_name,
            'time_zone': self.time_zone,
            'deep_logging': self.deep_logging,
            'msg': self._class_msg.build_data(),
            'xp': self.xp,
            'level_up_notification': self.level_up_notification,
            'level': self.level,
            'role': self.role,
            'bits': self.bits,
            'swear_words_counter': self.swear_words_counter,
            'swear_words_xp': self.swear_words_xp,
            'swear_words': self.swear_words,
            'toxicity_rank': self.toxicity_rank,
            'soft_warnings': self.soft_warnings,
            'hard_warnings': self.hard_warnings,
            'admin_warnings': self.admin_warnings,
            'gender': self.gender,
            'age': self.age,
            'country': self.country,
            'speak_in_vc': self.speak_in_vc
        }

        collection = self.client[self.scope][self.table]
        query = {'_id': self.user_id}
        cursor = collection.find(query)
        user_data_in_db = None
        for doc in cursor:
            user_data_in_db = doc
        if user_data_in_db is not None:
            user_data.pop("_id")
            collection.update_one(query, {'$set': user_data})
        else:
            collection.insert_one(user_data)

    def get_user_data(self):

        collection = self.client[self.scope][self.table]
        cursor = collection.find({'_id': self.user_id})
        user_data = None
        for doc in cursor:
            user_data = doc
        if user_data is None:
            return

        self.user_name = user_data.get('user_name', self.user_name)
        self.time_zone = user_data.get('time_zone', self.time_zone)
        self.deep_logging = user_data.get('deep_logging', self.deep_logging)
        self.msg = self._class_msg.extract_data(user_data.get('msg', self._class_msg.build_data()))
        self.xp = user_data.get('xp', self.xp)
        self.level_up_notification = user_data.get('level_up_notification', self.level_up_notification)
        self.level = user_data.get('level', self.level)
        self.role = user_data.get('role', self.role)
        self.bits = user_data.get('bits', self.bits)
        self.swear_words_counter = user_data.get('swear_words_counter', self.swear_words_counter)
        self.swear_words_xp = user_data.get('swear_words_xp', self.swear_words_xp)
        self.swear_words = user_data.get('swear_words', self.swear_words)
        self.toxicity_rank = user_data.get('toxicity_rank', self.toxicity_rank)
        self.soft_warnings = user_data.get('soft_warnings', self.soft_warnings)
        self.hard_warnings = user_data.get('hard_warnings', self.hard_warnings)
        self.admin_warnings = user_data.get('admin_warnings', self.admin_warnings)
        self.gender = user_data.get('gender', self.gender)
        self.age = user_data.get('age', self.age)
        self.country = user_data.get('country', self.country)
        self.speak_in_vc = user_data.get('speak_in_vc', self.speak_in_vc)


class MessagesCounters(object):

    def __init__(self):

        self.log_time_by_hour = []
        self.by_hour = []
        self.time_spent_by_hour = []

        self.log_time_by_day = []
        self.by_day = []
        self.time_spent_by_day = []

        self.log_time_by_month = []
        self.by_month = []
        self.time_spent_by_month = []

        self.commands = 0
        self.override = 0
        self.sudo = 0
        self.img = 0
        self.links = 0

    def extract_data(self, raw_data):
        self.log_time_by_hour = raw_data.get('log_time_by_hour', self.log_time_by_hour)
        self.by_hour = raw_data.get('by_hour', self.by_hour)
        self.time_spent_by_hour = raw_data.get('time_spent_by_hour', self.time_spent_by_hour)

        self.log_time_by_day = raw_data.get('log_time_by_day', self.log_time_by_day)
        self.by_day = raw_data.get('by_day', self.by_day)
        self.time_spent_by_day = raw_data.get('time_spent_by_day', self.time_spent_by_day)

        self.log_time_by_month = raw_data.get('log_time_by_month', self.log_time_by_month)
        self.by_month = raw_data.get('by_month', self.by_month)
        self.time_spent_by_month = raw_data.get('time_spent_by_month', self.time_spent_by_month)

        self.commands = raw_data.get('commands', self.commands)
        self.override = raw_data.get('override', self.override)
        self.sudo = raw_data.get('sudo', self.sudo)
        self.img = raw_data.get('img', self.img)
        self.links = raw_data.get('links', self.links)

        return self

    def build_data(self):

        data_out = {
            'log_time_by_hour': self.log_time_by_hour,
            'by_hour': self.by_hour,
            'time_spent_by_hour': self.time_spent_by_hour,

            'log_time_by_day': self.log_time_by_day,
            'by_day': self.by_day,
            'time_spent_by_day': self.time_spent_by_day,

            'log_time_by_month': self.log_time_by_month,
            'by_month': self.by_month,
            'time_spent_by_month': self.time_spent_by_month,

            'commands': self.commands,
            'override': self.override,
            'sudo': self.sudo,
            'img': self.img,
            'links': self.links,
        }

        return data_out
