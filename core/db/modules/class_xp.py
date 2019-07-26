class XpField(object):

    def __init__(self):

        self.level_up_notification = False
        self.xp_value = 10
        self.xp_toxicity = 0
        self.level = 0
        self.level_toxicity = 0
        self.role_by_xp = 0
        self.time_at_last_level_check = None
        self.level_at_last_check = None
        self.time_at_last_rank_check = None
        self.rank_at_last_check = None

    def extract_data(self, raw_data):
        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.xp_value = raw_data.get('xp', self.xp_value)
        self.xp_toxicity = raw_data.get('xp_toxicity', self.xp_toxicity)
        self.level = raw_data.get('level', self.level)
        self.level_toxicity = raw_data.get('level_toxicity', self.level_toxicity)
        self.role_by_xp = raw_data.get('role_by_xp', self.role_by_xp)
        self.time_at_last_level_check = raw_data.get('time_at_last_level_check', self.time_at_last_level_check)
        self.level_at_last_check = raw_data.get('level_at_last_check', self.level_at_last_check)
        self.time_at_last_rank_check = raw_data.get('time_at_last_rank_check', self.time_at_last_rank_check)
        self.rank_at_last_check = raw_data.get('rank_at_last_check', self.rank_at_last_check)

        return self

    def build_data(self):

        data_out = {
            'level_up_notification': self.level_up_notification,
            'xp': self.xp_value,
            'xp_toxicity': self.xp_toxicity,
            'level': self.level,
            'level_toxicity': self.level_toxicity,
            'role_by_xp': self.role_by_xp,
            'time_at_last_level_check': self.time_at_last_level_check,
            'level_at_last_check': self.level_at_last_check,
            'time_at_last_rank_check': self.time_at_last_rank_check,
            'rank_at_last_check': self.rank_at_last_check,
        }

        return data_out

    # level_up_notification
    @property
    def level_up_notification(self):
        return self.__level_up_notification

    @level_up_notification.setter
    def level_up_notification(self, value):
        self.__level_up_notification = value

    # xp_value
    @property
    def xp_value(self):
        return self.__xp_value

    @xp_value.setter
    def xp_value(self, value):
        self.__xp_value = value

    # xp_toxicity
    @property
    def xp_toxicity(self):
        return self.__xp_toxicity

    @xp_toxicity.setter
    def xp_toxicity(self, value):
        self.__xp_toxicity = value

    # level
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    # level_toxicity
    @property
    def level_toxicity(self):
        return self.__level_toxicity

    @level_toxicity.setter
    def level_toxicity(self, value):
        self.__level_toxicity = value

    # role_by_xp
    @property
    def role_by_xp(self):
        return self.__role_by_xp

    @role_by_xp.setter
    def role_by_xp(self, value):
        self.__role_by_xp = value

    # time_at_last_level_check
    @property
    def time_at_last_level_check(self):
        return self.__time_at_last_level_check

    @time_at_last_level_check.setter
    def time_at_last_level_check(self, value):
        self.__time_at_last_level_check = value

    # level_at_last_check
    @property
    def level_at_last_check(self):
        return self.__level_at_last_check

    @level_at_last_check.setter
    def level_at_last_check(self, value):
        self.__level_at_last_check = value

    # time_at_last_rank_check
    @property
    def time_at_last_rank_check(self):
        return self.__time_at_last_rank_check

    @time_at_last_rank_check.setter
    def time_at_last_rank_check(self, value):
        self.__time_at_last_rank_check = value

    # rank_at_last_check
    @property
    def rank_at_last_check(self):
        return self.__rank_at_last_check

    @rank_at_last_check.setter
    def rank_at_last_check(self, value):
        self.__rank_at_last_check = value

