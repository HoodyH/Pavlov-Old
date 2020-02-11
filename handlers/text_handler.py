from handlers.base_handler import BaseHandler


class TextHandler(BaseHandler):
    """
    It will handle the operations on the text.
    """
    def __init__(self, update, bot):
        super().__init__(update, bot)

    def handle(self):
        text = self.update.message.text  # get text form the message
        self.bsu.update_text(text)  # update stats
        self.check_commands(text)
        self.check_level_up()
