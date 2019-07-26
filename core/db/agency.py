from core.db.query import (push_data, pull_data)
from core.db.modules.class_message import MessagesField


class AgencyData(object):

    def __init__(self, client, scope, user_id):

        self.client = client
        self.scope = scope
        self.user_id = user_id

        self.table = str(user_id)

        # user data logging
        self.on_monitoring = True
        self.user_name = None
        self.commissions = []
        self.deep_logging = True

        self.__msg_field = MessagesField()
        self.msg = self.__msg_field

        self.get_data()

    def set_data(self):

        data = {
            '_id': self.user_id,
            'on_monitoring': self.on_monitoring,
            'user_name': self.user_name,
            'commissions': self.commissions,
            'deep_logging': self.deep_logging,

            'msg': self.__msg_field.build_data(),

        }

        push_data(self.client, self.scope, self.table, self.user_id, data)

    def get_data(self):

        data = pull_data(self.client, self.scope, self.table, self.user_id)

        self.on_monitoring = data.get('on_monitoring', self.on_monitoring)
        self.user_name = data.get('user_name', self.user_name)
        self.commissions = data.get('commissions', self.commissions)
        self.deep_logging = data.get('deep_logging', self.deep_logging)

        self.msg = self.__msg_field.extract_data(data.get('msg', self.__msg_field.build_data()))

    # on_monitoring
    @property
    def on_monitoring(self):
        return self.__on_monitoring

    @on_monitoring.setter
    def on_monitoring(self, value):
        self.__on_monitoring = value

    # user_name
    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    # commissions
    @property
    def commissions(self):
        return self.__commissions

    @commissions.setter
    def commissions(self, value):
        self.__commissions = value

    # deep_logging
    @property
    def deep_logging(self):
        return self.__deep_logging

    @deep_logging.setter
    def deep_logging(self, value):
        self.__deep_logging = value

    # msg
    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value
