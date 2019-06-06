
class UserData(object):

    def __init__(self, client, scope, guild_id, user_id):

        self.client = client
        self.scope = scope
        self.guild_id = guild_id
        self.user_id = user_id

        self.table = "bot_directs"

        # user data logging
        self.user_name = None
        self.deep_logging = True
        self.msg_total = 0
        self.msg_commands = 0
        self.msg_override = 0
        self.msg_sudo = 0
        self.msg_img = 0
        self.msg_links = 0
        self.xp = 0
        self.level_up_notification = False
        self.level = 0
        self.time_spent_sec = 0
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

        if self.guild_id is None:
            self.guild_id = self.table

        user_data = {
            '_id': self.user_id,
            'user_name': self.user_name,
            'deep_logging': self.deep_logging,
            'msg_total': self.msg_total,
            'msg_commands': self.msg_commands,
            'msg_override': self.msg_override,
            'msg_sudo': self.msg_sudo,
            'msg_img': self.msg_img,
            'msg_links': self.msg_links,
            'xp': self.xp,
            'level_up_notification': self.level_up_notification,
            'level': self.level,
            'time_spent_sec': self.time_spent_sec,
            'role': self.role,
            'bits': self.msg_total,
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

        collection = self.client[self.scope][str(self.guild_id)]
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

        if self.guild_id is None:
            self.guild_id = self.table

        collection = self.client[self.scope][str(self.guild_id)]
        cursor = collection.find({'_id': self.user_id})
        user_data = None
        for doc in cursor:
            user_data = doc
        if user_data is None:
            return

        self.user_name = user_data.get('user_name', self.user_name)
        self.deep_logging = user_data.get('deep_logging', self.deep_logging)
        self.msg_total = user_data.get('msg_total', self.msg_total)
        self.msg_commands = user_data.get('msg_commands', self.msg_commands)
        self.msg_override = user_data.get('msg_override', self.msg_override)
        self.msg_sudo = user_data.get('msg_sudo', self.msg_sudo)
        self.msg_img = user_data.get('msg_img', self.msg_img)
        self.msg_links = user_data.get('msg_links', self.msg_links)
        self.xp = user_data.get('xp', self.xp)
        self.level_up_notification = user_data.get('level_up_notification', self.level_up_notification)
        self.level = user_data.get('level', self.level)
        self.time_spent_sec = user_data.get('time_spent_sec', self.time_spent_sec)
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
