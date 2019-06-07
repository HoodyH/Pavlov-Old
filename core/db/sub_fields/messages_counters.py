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

        self.log_time_by_day = raw_data.get('log_time_by_day', self.log_time_by_day)
        self.by_month = raw_data.get('by_month', self.by_month)
        self.by_hour = raw_data.get('by_hour', self.by_hour)

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
