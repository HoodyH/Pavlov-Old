class User(object):

    def __init__(self,
                 id=None,
                 first_name=None,
                 is_bot=None,
                 **kwargs):

        self.id = id
        self.first_name = first_name
        self.is_bot = is_bot
        # Optionals
        self.last_name = kwargs.get("last_name", None)
        self.username = kwargs.get("username", None)
        self.language_code = kwargs.get("language_code", None)
        self.bot = kwargs.get("bot", None)

    def extract_data(self, raw_data):
        self.id = raw_data["id"]
        return self

    @property
    def user_id(self):
        """
        get user id as property
        """
        if self.id:
            return self.id

    @property
    def name(self):
        """
        get name as property
        """
        if self.username:
            return '@{}'.format(self.username)
        return self.full_name

    @property
    def full_name(self):
        """
        get full name
        """

        if self.last_name:
            return u'{} {}'.format(self.first_name, self.last_name)
        return self.first_name

    def send_message(self, message, **kwargs):
        """
        Send message directly to the user

        """
        return self.bot.send_message(self.id, message, **kwargs)