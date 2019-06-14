class XpField(object):

    def __init__(self):

        self.level_up_notification = False
        self.xp_value = 10
        self.level = 0
        self.role_by_xp = 0

    def extract_data(self, raw_data):
        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.xp_value = raw_data.get('xp', self.xp_value)
        self.level = raw_data.get('level', self.level)
        self.role_by_xp = raw_data.get('role_by_xp', self.role_by_xp)

        return self

    def build_data(self):

        data_out = {
            'level_up_notification': self.level_up_notification,
            'xp': self.xp_value,
            'level': self.level,
            'role_by_xp': self.role_by_xp,
        }

        return data_out

    # level_up_notification
    @property
    def level_up_notification(self):
        return self.__level_up_notification

    @level_up_notification.setter
    def level_up_notification(self, value):
        self.__level_up_notification = value

    # bits
    @property
    def xp_value(self):
        return self.__xp_value

    @xp_value.setter
    def xp_value(self, value):
        self.__xp_value = value

    # last_bit_farm
    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    # role_by_xp
    @property
    def role_by_xp(self):
        return self.__role_by_xp

    @role_by_xp.setter
    def role_by_xp(self, value):
        self.__role_by_xp = value
