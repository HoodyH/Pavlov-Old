from handlers.base_handler import BaseHandler


class TextHandler(BaseHandler):
    """
    Middle point to prepare data that have to be saved to the database
    This is an interface between the platform-wrapper and the pvlv_database

    This Handler will handle the operations on the text.
    Like:
     - stats updating
     - command reading
     - text interactions
    """
    def __init__(self, update, bot):
        super().__init__(update, bot)

    def handle(self):
        text = self.update.message.text
        self.bsu.update_text(text)
        self.check_commands(text)
        self.check_level_up()
