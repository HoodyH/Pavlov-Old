from core.db.modules.class_message import MessagesField
from core.db.modules.class_xp import XpField
from core.db.modules.class_bill import BillField

from pprint import pprint


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

        self.__msg_field = MessagesField()
        self.msg = self.__msg_field

        self.__xp_field = XpField()
        self.xp = self.__xp_field

        self.__bill_field = BillField()
        self.bill = self.__bill_field

        self.get_user_data()

    def set_user_data(self):

        user_data = {
            '_id': self.user_id,
            'user_name': self.user_name,
            'time_zone': self.time_zone,
            'deep_logging': self.deep_logging,

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
            'speak_in_vc': self.speak_in_vc,

            'msg': self.__msg_field.build_data(),
            'xp': self.__xp_field.build_data(),
            'bill': self.__bill_field.build_data(),
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

        self.msg = self.__msg_field.extract_data(user_data.get('msg', self.__msg_field.build_data()))
        data = self.__xp_field.build_data()
        self.xp = self.__xp_field.extract_data(user_data.get('xp', data))
        self.bill = self.__bill_field.extract_data(user_data.get('bill', self.__bill_field.build_data()))

    def get_user_rank(self):
        collection = self.client[self.scope][self.table]
        try:
            cursor = collection.find({"$query": {}, "$orderby": {"xp.xp": -1}})
        except Exception as e:
            print(e)
            return 'N/D'

        rank_counter = 1
        for doc in cursor:
            user_id = doc.get('_id')
            if user_id == self.user_id:
                return rank_counter
            rank_counter += 1

        return 'N/D'

    def build_ranking(self, limit=10):
        collection = self.client[self.scope][self.table]
        try:
            cursor = collection.find({"$query": {}, "$orderby": {"xp.xp": -1}})
        except Exception as e:
            print(e)
            return 'N/D'

        rank_counter = 1
        data = {}
        for doc in cursor:
            user_id = doc.get('_id')
            data[rank_counter] = {
                'username': doc.get('user_name'),
                'highlights': True if user_id == self.user_id else False,
                'rank': rank_counter,
                'level': doc.get('xp').get('level'),
                'value': doc.get('xp').get('xp')
            }
            if limit == rank_counter:
                return data
            rank_counter += 1
        return data

    # user_name
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    # time_zone
    @property
    def time_zone(self):
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, value):
        self.__time_zone = value

    # deep_logging
    @property
    def deep_logging(self):
        return self.__deep_logging

    @deep_logging.setter
    def deep_logging(self, value):
        self.__deep_logging = value

    # swear_words_counter
    @property
    def swear_words_counter(self):
        return self.__swear_words_counter

    @swear_words_counter.setter
    def swear_words_counter(self, value):
        self.__swear_words_counter = value

    # swear_words_xp
    @property
    def swear_words_xp(self):
        return self.__swear_words_xp

    @swear_words_xp.setter
    def swear_words_xp(self, value):
        self.__swear_words_xp = value

    # swear_words
    @property
    def swear_words(self):
        return self.__swear_words

    @swear_words.setter
    def swear_words(self, value):
        self.__swear_words = value

    # toxicity_rank
    @property
    def toxicity_rank(self):
        return self.__toxicity_rank

    @toxicity_rank.setter
    def toxicity_rank(self, value):
        self.__toxicity_rank = value

    # soft_warnings
    @property
    def soft_warnings(self):
        return self.__soft_warnings

    @soft_warnings.setter
    def soft_warnings(self, value):
        self.__soft_warnings = value

    # hard_warnings
    @property
    def hard_warnings(self):
        return self.__hard_warnings

    @hard_warnings.setter
    def hard_warnings(self, value):
        self.__hard_warnings = value

    # admin_warnings
    @property
    def admin_warnings(self):
        return self.__admin_warnings

    @admin_warnings.setter
    def admin_warnings(self, value):
        self.__admin_warnings = value

    # gender
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    # age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    # country
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    # speak_in_vc
    @property
    def speak_in_vc(self):
        return self.__speak_in_vc

    @speak_in_vc.setter
    def speak_in_vc(self, value):
        self.__speak_in_vc = value

    # msg
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value

    # xp
    @property
    def xp(self):
        return self.__xp

    @xp.setter
    def xp(self, value):
        self.__xp = value

    # bill
    @property
    def bill(self):
        return self.__bill

    @bill.setter
    def bill(self, value):
        self.__bill = value
