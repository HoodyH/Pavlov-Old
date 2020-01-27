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
            'unique_id': self.user_id,
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
