class Chat(object):

    def __init__(self,
                id=None,
                **kwargs):
        self.id = id
        self.title = kwargs.get("title", None)

    def extract_data(self, raw_data):
        self.id = raw_data["id"]
        self.title = raw_data["title"]
        return self
