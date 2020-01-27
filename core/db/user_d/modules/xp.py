class XpData(object):

    def __init__(self):

        self.level_up_notification = False
        self.xp_value = 10
        self.level = 0

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
