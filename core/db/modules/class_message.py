class MessagesField(object):

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
        self.documents = 0
        self.vocals = 0
        self.video_note = 0
        self.stickers = 0

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
        self.documents = raw_data.get('documents', self.documents)
        self.vocals = raw_data.get('vocals', self.vocals)
        self.video_note = raw_data.get('video_note', self.video_note)
        self.stickers = raw_data.get('stickers', self.stickers)

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
            'documents': self.documents,
            'vocals': self.vocals,
            'video_note': self.video_note,
            'stickers': self.stickers,
        }

        return data_out

    # log_time_by_hour
    @property
    def log_time_by_hour(self):
        return self.__log_time_by_hour

    @log_time_by_hour.setter
    def log_time_by_hour(self, value):
        self.__log_time_by_hour = value

    # by_hour
    @property
    def by_hour(self):
        return self.__by_hour

    @by_hour.setter
    def by_hour(self, value):
        self.__by_hour = value

    # time_spent_by_hour
    @property
    def time_spent_by_hour(self):
        return self.__time_spent_by_hour

    @time_spent_by_hour.setter
    def time_spent_by_hour(self, value):
        self.__time_spent_by_hour = value

    # log_time_by_day
    @property
    def log_time_by_day(self):
        return self.__log_time_by_day

    @log_time_by_day.setter
    def log_time_by_day(self, value):
        self.__log_time_by_day = value

    # by_day
    @property
    def by_day(self):
        return self.__by_day

    @by_day.setter
    def by_day(self, value):
        self.__by_day = value

    # time_spent_by_day
    @property
    def time_spent_by_day(self):
        return self.__time_spent_by_day

    @time_spent_by_day.setter
    def time_spent_by_day(self, value):
        self.__time_spent_by_day = value

    # log_time_by_month
    @property
    def log_time_by_month(self):
        return self.__log_time_by_month

    @log_time_by_month.setter
    def log_time_by_month(self, value):
        self.__log_time_by_month = value

    # by_month
    @property
    def by_month(self):
        return self.__by_month

    @by_month.setter
    def by_month(self, value):
        self.__by_month = value

    # time_spent_by_month
    @property
    def time_spent_by_month(self):
        return self.__time_spent_by_month

    @time_spent_by_month.setter
    def time_spent_by_month(self, value):
        self.__time_spent_by_month = value

    # commands
    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    # override
    @property
    def override(self):
        return self.__override

    @override.setter
    def override(self, value):
        self.__override = value

    # sudo
    @property
    def sudo(self):
        return self.__sudo

    @sudo.setter
    def sudo(self, value):
        self.__sudo = value

    # img
    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, value):
        self.__img = value

    # links
    @property
    def links(self):
        return self.__links

    @links.setter
    def links(self, value):
        self.__links = value

    # documents
    @property
    def documents(self):
        return self.__documents

    @documents.setter
    def documents(self, value):
        self.__documents = value

    # vocals
    @property
    def vocals(self):
        return self.__vocals

    @vocals.setter
    def vocals(self, value):
        self.__vocals = value

    # video_note
    @property
    def video_note(self):
        return self.__video_note

    @video_note.setter
    def video_note(self, value):
        self.__video_note = value

    # stickers
    @property
    def stickers(self):
        return self.__stickers

    @stickers.setter
    def stickers(self, value):
        self.__stickers = value
