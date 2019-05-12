class Message():
    """
    This object represents a message.
    """

    def __init__(self, **kwargs):
        self.message_id = kwargs.get("message_id", None)
        self.from_user = kwargs.get("from_user", None)
        self.chat = kwargs.get("chat", None)
        self.text = kwargs.get("text", None)


    def reply_text(self, msg, chat_id):
        return self.bot.send_message(msg, chat_id)
