from skills.core.utils.formatting import from_timestamp

from telegram.user import User
from telegram.chat import Chat

class Message(object):
    """
    This object represents a message.
    """

    def __init__(self,
                bot,
                message_id=None,
                user=None,
                date=None,
                chat=None,
                **kwargs):
        self.bot = bot
        self.message_id = message_id
        self.user = user
        self.date = date
        self.chat = chat
        self.text = kwargs.get("text", None)


    def extract_data(self, raw_data):
        user = User()
        chat = Chat()
        try:
            message = raw_data["message"]
            self.message_id = message["message_id"]
            self.user = user.extract_data(message["from"])
            self.date = from_timestamp(message["date"])
        except: 
            message = None
            self.message_id = None
            self.user = None
            self.date = None
        
        try:
            self.chat = chat.extract_data(message["chat"])
        except: 
            self.chat = None 
        try:
            self.text = message["text"]
        except:
            self.text = None

        return self


    def send_text(self, text):
        if self.chat is not None:
            return self.bot.send_message(self.chat.id, text)
        elif self.user is not None:
            return self.bot.send_message(self.user.id, text)
        else:
            return None
