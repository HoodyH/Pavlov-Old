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

        self.output_permission = True

        self.message_on_same_chat = None
        self.message_on_guild = None

    def update_bot_data(self, scope, bot, message):

        self._scope = scope
        self._bot = bot
        self._message = message

        if self.scope == TELEGRAM:
            self._guild = Guild(self.scope, message)
            self._chat = self._guild
            self._user = User(self.scope, message)
        elif self.scope == DISCORD:
            self._guild = None
            self._chat = None
            self._user = None

        if self.chat.id is not None:
            self.message_on_same_chat = self.chat.id
        elif self.guild.id is not None:
            self.message_on_same_chat = self.guild.id
            self.message_on_guild = self.guild.id
        else:
            self.message_on_same_chat = self.user.id

    def update_output_permission(self, pause_status):

        if pause_status is False:
            self.output_permission = True
        else:
            self.output_permission = False

    def choose_destination(self, send_function, destination, args):

        if self.scope == TELEGRAM:

            if destination == MSG_ON_DEFAULT_CHAT:
                send_function(self.message_on_guild, args)
            elif destination == MSG_ON_SAME_CHAT:
                send_function(self.message_on_same_chat, args)
            elif destination == MSG_DIRECT:
                send_function(self._user.id, args)
            else:
                send_function(destination, args)

        elif self.scope == DISCORD:
            return

        else:
            return

    def __telegram_send_photo(self, location, kwargs):

        img_bytes = kwargs.get('img_bytes')
        caption = kwargs.get('caption')
        # disable_notification = kwargs.get('disable_notification')
        # reply_to_message_id = kwargs.get('reply_to_message_id')
        # reply_markup = kwargs.get('reply_markup')
        # timeout = kwargs.get('timeout')
        # parse_mode = kwargs.get('parse_mode')

        try:
            self._bot.send_chat_action(chat_id=location, action=telegram.ChatAction.UPLOAD_PHOTO)
            self._bot.send_photo(
                chat_id=location,
                photo=img_bytes,
                caption=caption,
                # disable_notification=disable_notification,
                # reply_to_message_id=reply_to_message_id,
                # reply_markup=reply_markup,
                # timeout=timeout,
                # parse_mode=parse_mode,
                **kwargs
            )

        except Exception as e:
            print(e)

    def send_image(self,
                   img_bytes,
                   destination,
                   caption=None,
                   disable_notification=False,
                   reply_to_message_id=None,
                   reply_markup=None,
                   timeout=20,
                   parse_mode=None,
                   ):

        if self.output_permission is False:
            print('sender is disabled')
            return

        def send_photo(location):
            try:
                self._bot.send_chat_action(chat_id=location, action=telegram.ChatAction.UPLOAD_PHOTO)
                self._bot.send_photo(
                    chat_id=location,
                    photo=img_bytes,
                    caption=caption,
                    # disable_notification=disable_notification,
                    # reply_to_message_id=reply_to_message_id,
                    # reply_markup=reply_markup,
                    # timeout=timeout,
                    # parse_mode=parse_mode
                )

            except Exception as e:
                print(e)

        if self.scope == TELEGRAM:

            if destination == MSG_ON_DEFAULT_CHAT:
                send_photo(self.message_on_guild)
            elif destination == MSG_ON_SAME_CHAT:
                send_photo(self.message_on_same_chat)
            elif destination == MSG_DIRECT:
                send_photo(self._user.id)
            else:
                send_photo(destination)

        elif self.scope == DISCORD:
            return

        else:
            return

    def __telegram_send_message(self, location, kwargs):

        message = kwargs.get('message')
        write_en = kwargs.get('write_en')
        write_time_sec = kwargs.get('write_time_sec')
        parse_mode_en = kwargs.get('parse_mode_en')
        # disable_web_page_preview = kwargs.get('disable_web_page_preview')
        # disable_notification = kwargs.get('disable_notification')
        # reply_to_message_id = kwargs.get('reply_to_message_id')
        # reply_markup = kwargs.get('reply_markup')
        # timeout = kwargs.get('timeout')

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
                text=message.replace('**', '*') if parse_mode_en is True else message,
                parse_mode=telegram.ParseMode.MARKDOWN if parse_mode_en is True else None,
                # disable_web_page_preview=disable_web_page_preview,
                # disable_notification=disable_notification,
                # reply_to_message_id=reply_to_message_id,
                # reply_markup=reply_markup,
                # timeout=timeout,
                **kwargs
            )
        except Exception as e:
            print(e)

    def send_message(self,
                     message,
                     destination,
                     write_en=False,
                     write_time_sec=None,
                     parse_mode_en=False,
                     disable_web_page_preview=None,
                     disable_notification=False,
                     reply_to_message_id=None,
                     reply_markup=None,
                     timeout=None
                     ):

        if self.output_permission is False:
            print('sender is disabled')
            return

        args = {
            'message': message,
            'write_en': write_en,
            'write_time_sec': write_time_sec,
            'parse_mode_en': parse_mode_en,
            'disable_web_page_preview': disable_web_page_preview,
            'disable_notification': disable_notification,
            'reply_to_message_id': reply_to_message_id,
            'reply_markup': reply_markup,
            'timeout': timeout
        }

        self.choose_destination(self.__telegram_send_message, destination, args)

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
