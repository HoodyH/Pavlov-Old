from core.db.submodule.action_counter_log import ActionCounterLog


class MessagesField(object):

    def __init__(self):

        self.msg_log = ActionCounterLog()
        self.img_log = ActionCounterLog()
        self.links_log = ActionCounterLog()
        self.vocals_log = ActionCounterLog()

        self.swear_words_log = ActionCounterLog()
        self.swear_words = {}

        self.most_used_words = {}

    def extract_data(self, raw_data):

        self.msg_log = ActionCounterLog().extract_data(raw_data.get('msg_log'))
        if not self.msg_log:
            self.msg_log = ActionCounterLog().build_data()

        self.img_log = ActionCounterLog().extract_data(raw_data.get('img_log'))
        if not self.img_log:
            self.img_log = ActionCounterLog().build_data()

        self.links_log = ActionCounterLog().extract_data(raw_data.get('links_log'))
        if not self.links_log:
            self.links_log = ActionCounterLog().build_data()

        self.vocals_log = ActionCounterLog().extract_data(raw_data.get('vocals_log'))
        if not self.vocals_log:
            self.vocals_log = ActionCounterLog().build_data()

        self.swear_words_log = ActionCounterLog().extract_data(raw_data.get('swear_words_log'))
        if not self.swear_words_log:
            self.swear_words_log = ActionCounterLog().build_data()

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
