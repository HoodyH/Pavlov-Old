class XpData(object):

    def __init__(self):

        self.level_up_notification = False
        self.xp_value = 10
        self.level = 0

        self.__is_level_up = False  # internal value, it go true when there is a level up

    def extract_data(self, raw_data):

        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.xp_value = raw_data.get('xp', self.xp_value)
        self.level = raw_data.get('level', self.level)

        return self

    def build_data(self):

        data_out = {
            'level_up_notification': self.level_up_notification,
            'xp': self.xp_value,
            'level': self.level,
        }

        return data_out

    @property
    def is_level_up(self):
        """
        Check if is time to level up, once controlled it will auto reset.
        You will find this true only once.
        :return: True or False
        """
        if self.__is_level_up:
            self.__is_level_up = False
            return True
        return False
