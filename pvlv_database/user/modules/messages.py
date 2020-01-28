from pvlv_database.common.action_counter_log import ActionCounterLog


class MessagesData(object):

    def __init__(self):

        self.msg_log = ActionCounterLog()
        self.img_log = ActionCounterLog()
        self.links_log = ActionCounterLog()
        self.vocals_log = ActionCounterLog()

        self.swear_words_log = ActionCounterLog()
        self.swear_words = {}

        self.most_used_words = {}

    def extract_data(self, raw_data):

        msg_log = raw_data.get('msg_log')
        self.msg_log = ActionCounterLog() if not msg_log else ActionCounterLog().extract_data(msg_log)

        img_log = raw_data.get('img_log')
        self.img_log = ActionCounterLog() if not img_log else ActionCounterLog().extract_data(img_log)

        links_log = raw_data.get('links_log')
        self.links_log = ActionCounterLog() if not links_log else ActionCounterLog().extract_data(links_log)

        vocals_log = raw_data.get('vocals_log')
        self.vocals_log = ActionCounterLog() if not vocals_log else ActionCounterLog().extract_data(vocals_log)

        swear_words_log = raw_data.get('swear_words_log')
        self.swear_words_log = ActionCounterLog() if not swear_words_log else ActionCounterLog().extract_data(swear_words_log)

        self.swear_words = raw_data.get('swear_words', self.swear_words)

        self.most_used_words = raw_data.get('most_used_words', self.most_used_words)

        return self

    def build_data(self):

        data_out = {

            'msg_log': self.msg_log.build_data(),
            'img_log': self.img_log.build_data(),
            'links_log': self.links_log.build_data(),
            'vocals_log': self.vocals_log.build_data(),

            'swear_words_log': self.swear_words_log.build_data(),
            'swear_words': self.swear_words,

            'most_used_words': self.most_used_words,
        }

        return data_out
