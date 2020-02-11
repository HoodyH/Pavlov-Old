from handlers.base_handler import BaseHandler


class ImgHandler(BaseHandler):
    """
    It will handle the operations on images.
    """
    def __init__(self, update, bot):
        super().__init__(update, bot)

    def handle(self):
        caption = self.update.message.caption  # the text under the photo
        self.bsu.update_image()  # update stats

        if caption:
            self.bsu.update_text(caption)
            self.check_commands(caption)
        self.check_level_up()
