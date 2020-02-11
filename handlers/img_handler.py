from handlers.base_handler import BaseHandler


class ImgHandler(BaseHandler):
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
        caption = self.update.message.caption  # the text in the photo
        self.bsu.update_image()

        if caption:
            self.bsu.update_text(caption)
            self.check_commands(caption)
        self.check_level_up()
