from core.db.modules.commands import CommandsField
from core.db.user_d.modules.messages import MessagesField
from core.db.modules.class_xp import XpField
from core.db.modules.class_bill import BillField


class GuildUser(object):

    def __init__(self):
        # user data logging
        self.guild_id = None
        self.guild_name = ''
        self.permissions = 10

        self.commands = CommandsField()
        self.msg = MessagesField()

        # self.xp = XpField()
        # self.bill = BillField()

    def extract_data(self, raw_data):
        self.guild_id = raw_data.get('guild_id', self.guild_id)
        self.guild_name = raw_data.get('guild_name', self.guild_name)
        self.permissions = raw_data.get('permissions', self.permissions)

        self.commands = CommandsField().extract_data(raw_data.get('commands'))
        if not self.commands:
            self.commands = CommandsField().build_data()

        self.msg = MessagesField().extract_data(raw_data.get('msg'))
        if not self.msg:
            self.msg = MessagesField().build_data()

        """
        self.xp = XpField().extract_data(raw_data.get('xp'))
        if not self.xp:
            self.xp = XpField().build_data()
        
        self.bill = BillField().extract_data(raw_data.get('bill'))
        if not self.bill:
            self.bill = BillField().build_data()
        """

        return self

    def build_data(self):

        data = {
            'guild_id': self.guild_id,
            'guild_name': self.guild_name,
            'permissions': self.permissions,

            'commands': self.commands.build_data(),
            'msg': self.msg.build_data(),

            # 'xp': self.__xp_field.build_data(),
            # 'bill': self.__bill_field.build_data(),

        }

        return data
