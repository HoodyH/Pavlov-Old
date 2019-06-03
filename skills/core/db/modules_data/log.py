class Log(object):

    def __init__(self):

        self.level_up_notification = True
        self.level_up_destination = 0
        self.start_notifications_at_level = 5
        self.bits_min_add = 0
        self.bits_max_add = 4
        self.use_global_bits = True
        self.member_total = 0
        self.msg_total = 0
        self.msg_commands = 0
        self.msg_override = 0
        self.msg_sudo = 0
        self.msg_img = 0
        self.msg_links = 0

    def extract_data(self, raw_data):
        self.level_up_notification = raw_data.get('level_up_notification', self.level_up_notification)
        self.level_up_destination = raw_data.get('level_up_destination', self.level_up_destination)
        self.start_notifications_at_level = raw_data.get('start_notifications_at_level', self.start_notifications_at_level)
        self.bits_min_add = raw_data.get('bits_min_add', self.bits_min_add)
        self.bits_max_add = raw_data.get('bits_max_add', self.bits_max_add)
        self.use_global_bits = raw_data.get('use_global_bits', self.use_global_bits)
        self.member_total = raw_data.get('member_total', self.member_total)
        self.msg_total = raw_data.get('msg_total', self.msg_total)
        self.msg_commands = raw_data.get('msg_commands', self.msg_commands)
        self.msg_override = raw_data.get('msg_override', self.msg_override)
        self.msg_sudo = raw_data.get('msg_sudo', self.msg_sudo)
        self.msg_img = raw_data.get('msg_img', self.msg_img)
        self.msg_links = raw_data.get('msg_links', self.msg_links)

        return self

    def build_data(self):

        data_out = {
            'level_up_notification': self.level_up_notification,
            'level_up_destination': self.level_up_destination,
            'start_notifications_at_level': self.start_notifications_at_level,
            'bits_min_add': self.bits_min_add,
            'bits_max_add': self.bits_max_add,
            'use_global_bits': self.use_global_bits,
            'member_total': self.member_total,
            'msg_total': self.msg_total,
            'msg_commands': self.msg_commands,
            'msg_override': self.msg_override,
            'msg_sudo': self.msg_sudo,
            'msg_img': self.msg_img,
            'msg_links': self.msg_links,
        }

        return data_out
