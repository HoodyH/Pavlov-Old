import requests
import json
import configparser as cfg

class Bot():

    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.base_file_url = "https://api.telegram.org/file/bot{}/".format(self.token)


    """
    Method to get the bot informations
    """
    def get_me(self):
        url = self.base_url + "getMe"
        r = requests.get(url)
        return json.loads(r.content)

    """
    Method to receive incoming updates using long polling.
    An Array of Update objects is returned.

    kwargs:

    offset: int, optional (Defaults:100)
    Identifier of the first update to be returned. 
    Must be greater by one than the highest among the identifiers of previously received updates. 
    By default, updates starting with the earliest unconfirmed update are returned.

    limit: int, optional (Defaults:100)
    Limits the number of updates to be retrieved. Values between 1—100 are accepted

    timeout int, optional (Defaults:100)
    Timeout in seconds for long polling.

    allowed_updates, array of string optional [“message”, “edited_channel_post”, “callback_query”] (Defaults:all)
    List the types of updates you want your bot to receive.

    """
    def get_updates(self, **kwargs):
        self.offset = kwargs.get("offset", None)
        self.limit = kwargs.get("limit", None)
        self.timeout = kwargs.get("timeout", 100)
        self.allowed_updates = kwargs.get("allowed_updates", None)

        url = self.base_url + "getUpdates?"
        
        if self.offset is not None:
            url = url + "&offset={}".format(self.offset + 1)
        if self.limit is not None:
            url = url + "&limit={}".format(self.limit)
        if self.timeout is not None:
            url = url + "&timeout={}".format(self.timeout)
        if self.allowed_updates is not None:
            url = url + "&allowed_updates={}".format(self.allowed_updates)


        r = requests.get(url)
        return json.loads(r.content)


    def send_message(self, msg, chat_id):
        url = self.base_url + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)