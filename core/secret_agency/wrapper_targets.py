class Targets(object):
    def __init__(self, targets_data):

        self.targets_data = targets_data

        self.__monitoring = None
        self.__name = None
        self.__commissioners = None

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

    def is_under_monitoring_user(self, user_id):

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


class Commissioner(object):

    def __init__(self, data):

        self.data = data

        self.platform = None
        self.channel_id = None
        self.data_to_collect = None
        self.channel_restriction = None
        self.message_attached = None

        self.build_data()

    def build_data(self):

        self.platform = self.data.get('platform')
        self.channel_id = self.data.get('channel_id')
        self.data_to_collect = self.data.get('data_to_collect')
        self.channel_restriction = self.data.get('channel_restriction')
        self.message_attached = self.data.get('message_attached')
