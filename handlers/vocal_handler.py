from threading import Thread
from handlers.base_handler import BaseHandler
from handlers.speech_to_text.speech_to_text import speech_to_text


class VocalHandler(BaseHandler):
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

        # do fast stuff
        duration = self.update.message.voice.duration
        self.bsu.update_vocal(duration)
        self.check_level_up()

        # run the speech to text on another thread, cause it's time consuming operation
        file = self.bot.getFile(self.update.message.voice.file_id)
        t = Thread(target=speech_to_text, args=(self.bot, file, self.guild_id, self.db.guild.languages[0]))
        t.start()
