class CommissionField(object):

    def __init__(self):

        self.platform = None
        self.channel_id = None
        self.commissioners = []
        self.data_to_collect = []
        self.channel_restriction = []
        self.message_attached = ''
        self.notes = ''

    def extract_data(self, raw_data):
        self.platform = raw_data.get('platform', self.platform)
        self.channel_id = raw_data.get('channel_id', self.channel_id)
        self.commissioners = raw_data.get('commissioners', self.commissioners)
        self.data_to_collect = raw_data.get('data_to_collect', self.data_to_collect)
        self.channel_restriction = raw_data.get('channel_restriction', self.channel_restriction)
        self.message_attached = raw_data.get('message_attached', self.message_attached)
        self.notes = raw_data.get('notes', self.notes)

        return self

    def build_data(self):

        data_out = {
            'platform': self.platform,
            'channel_id': self.channel_id,
            'commissioners': self.commissioners,
            'data_to_collect': self.data_to_collect,
            'channel_restriction': self.channel_restriction,
            'message_attached': self.message_attached,
            'notes': self.notes,
        }

        return data_out

    # platform
    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    # channel_id
    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value):
        self.__channel_id = value

    # commissioners
    @property
    def commissioners(self):
        return self.__commissioners

    @commissioners.setter
    def commissioners(self, value):
        self.__commissioners = value

    # data_to_collect
    @property
    def data_to_collect(self):
        return self.__data_to_collect

    @data_to_collect.setter
    def data_to_collect(self, value):
        self.__data_to_collect = value

    # channel_restriction
    @property
    def channel_restriction(self):
        return self.__channel_restriction

    @channel_restriction.setter
    def channel_restriction(self, value):
        self.__channel_restriction = value

    # message_attached
    @property
    def message_attached(self):
        return self.__message_attached

    @message_attached.setter
    def message_attached(self, value):
        self.__message_attached = value

    # notes
    @property
    def notes(self):
        return self.__notes

    @notes.setter
    def notes(self, value):
        self.__notes = value

