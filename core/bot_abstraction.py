import telegram
from core.src.settings import *
from time import sleep


class User(object):
    def __init__(self, scope, message):

        if scope == TELEGRAM:
            self._id = message.from_user.id
            self._username = message.from_user.username
            self._is_bot = message.from_user.is_bot
            self._language_client = message.from_user.language_code
        else:
            self._id = None
            self._username = None
            self._is_bot = None
            self._language_client = None

    @property
    def id(self):
        return self._id

    @property
    def username(self):
        return self._username

    @property
    def is_bot(self):
        return self._is_bot

    @property
    def language_client(self):
        return self._language_client


class Guild(object):
    def __init__(self, scope, message):

        if scope == TELEGRAM:
            self._id = message.chat.id if message.chat.id != message.from_user.id else None
            self._guild_name = message.chat.title if message.chat.title is not None else None
        else:
            self._id = None
            self._guild_name = None

    @property
    def id(self):
        return self._id

    @property
    def guild_name(self):
        return self._guild_name


class BotStd(object):
    def __init__(self):

        self._scope = None
        self._bot = None
        self._message = None

        self._guild = None
        self._chat = None
        self._user = None

    def update_bot_data(self, scope, bot, message):

        self._scope = scope
        self._bot = bot
        self._message = message

        if self.scope == TELEGRAM:
            self._guild = Guild(self.scope, message)
            self._user = User(self.scope, message)
        elif self.scope == DISCORD:
            self._guild = None
            self._chat = None
            self._user = None

    def send_image(self,
                   img_bytes,
                   destination,
                   caption=None,
                   disable_notification=False,
                   reply_to_message_id=None,
                   reply_markup=None,
                   timeout=20,
                   parse_mode=None,
                   **kwargs
                   ):

        def __telegram_send(location):
            try:
                self._bot.send_chat_action(chat_id=location, action=telegram.ChatAction.UPLOAD_PHOTO)
                self._bot.send_photo(
                    chat_id=location,
                    photo=img_bytes,
                    caption=caption,
                    disable_notification=disable_notification,
                    reply_to_message_id=reply_to_message_id,
                    reply_markup=reply_markup,
                    timeout=timeout,
                    parse_mode=parse_mode,
                    ** kwargs
                )

            except Exception as e:
                print(e)

        if self.scope == TELEGRAM:

            if destination == MSG_ON_STATIC_CHAT:
                __telegram_send(self._message.chat.id)
            elif destination == MSG_ON_SAME_CHAT:
                __telegram_send(self._message.chat.id)
            else:
                __telegram_send(self._message.user.id)

        elif self.scope == DISCORD:
            return

        else:
            return

    def send_message(self,
                     message,
                     destination,
                     write_en=False,
                     write_time_sec=None,
                     parse_mode_en=False,
                     parse_mode=None,
                     disable_web_page_preview=None,
                     disable_notification=False,
                     reply_to_message_id=None,
                     reply_markup=None,
                     timeout=None,
                     **kwargs
                     ):

        def __telegram_send(location):

            try:

                if write_en is True:
                    if write_time_sec is not None:
                        while write_time_sec > 0:
                            self._bot.send_chat_action(chat_id=location, action=telegram.ChatAction.TYPING)
                            sleep(1)
                    else:
                        self._bot.send_chat_action(chat_id=location, action=telegram.ChatAction.TYPING)
                        sleep(0.5)

                # [inline mention of a user](tg://user?id=338674622)

                self._bot.send_message(
                    chat_id=location,
                    text=message.replace('**', '*'),
                    parse_mode=telegram.ParseMode.MARKDOWN if parse_mode_en is True else None,
                    disable_web_page_preview=disable_web_page_preview,
                    disable_notification=disable_notification,
                    reply_to_message_id=reply_to_message_id,
                    reply_markup=reply_markup,
                    timeout=timeout,
                    **kwargs
                    )
            except Exception as e:
                print(e)

        if self.scope == TELEGRAM:

            if destination == MSG_ON_STATIC_CHAT:
                __telegram_send(self._message.chat.id)
            elif destination == MSG_ON_SAME_CHAT:
                __telegram_send(self._message.chat.id)
            else:
                __telegram_send(self._message.user.id)

        elif self.scope == DISCORD:
            return

        else:
            return

    @property
    def guild(self):
        return self._guild

    @property
    def chat(self):
        return self._chat

    @property
    def user(self):
        return self._user

    @property
    def scope(self):
        return self._scope

    @property
    def message(self):
        return self._message

    @property
    def real_bot(self):
        return self._bot

