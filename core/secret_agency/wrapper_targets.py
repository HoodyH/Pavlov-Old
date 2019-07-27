class Targets(object):
    def __init__(self, targets_data):

        self.targets_data = targets_data

        self.__monitoring = None
        self.__name = None
        self.__commissioners = None
        self.last_member_update = None
        self.last_voice_state_update = None

    def update_target_data(self, target_id):

        target = self.targets_data.get(target_id, False)

        if target:

            self.__monitoring = target.get('monitoring')
            self.__name = target.get('name')
            self.__commissioners = []

            for el in target.get('commissioners'):
                self.__commissioners.append(Commissioner(el))
        else:
            self.__monitoring = None
            self.__name = None
            self.__commissioners = None
            raise Exception('Target not found')

    def is_under_monitoring(self, user_id):

        user_id = str(user_id)

        for key in self.targets_data.keys():
            if user_id == key:
                try:
                    self.update_target_data(key)
                except Exception as e:
                    print(e)
                if self.__monitoring:
                    return True
                break
        return False

    @property
    def monitoring(self):
        return self.__monitoring

    @property
    def name(self):
        return self.__name

    @property
    def commissioners(self):
        return self.__commissioners

    @property
    def last_member_update(self):
        return self.__last_member_update

    @last_member_update.setter
    def last_member_update(self, value):
        self.__last_member_update = value

    def changes_in_last_member_update(self, current_status):
        if current_status != self.last_member_update:
            self.last_member_update = current_status
            return True
        else:
            return False

    @property
    def last_voice_state_update(self):
        return self.__last_voice_state_update

    @last_voice_state_update.setter
    def last_voice_state_update(self, value):
        self.__last_voice_state_update = value

    def changes_in_last_voice_state_update(self, current_status):
        if current_status != self.last_voice_state_update:
            self.last_voice_state_update = current_status
            return True
        else:
            return False


class Commissioner(object):

    def __init__(self, data):

        self.data = data

        self.__platform = None
        self.__channel_id = None
        self.__data_to_collect = None
        self.__channel_restriction = None
        self.__message_attached = None

        self.extract_data()

    def extract_data(self):

        self.__platform = self.data.get('platform')
        self.__channel_id = self.data.get('channel_id')
        self.__data_to_collect = self.data.get('data_to_collect')
        self.__channel_restriction = self.data.get('channel_restriction')
        self.__message_attached = self.data.get('message_attached')

    @property
    def platform(self):
        return self.__platform

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def data_to_collect(self):
        return self.__data_to_collect

    @property
    def channel_restriction(self):
        return self.__channel_restriction

    @property
    def message_attached(self):
        return self.__message_attached
