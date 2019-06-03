import requests
import json


class Bot(object):

    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.telegram.org/bot{}/".format(self.token)
        self.base_file_url = "https://api.telegram.org/file/bot{}/".format(self.token)
        self._request = requests


    """
    Method to get the bot informations
    """
    def get_me(self):
        url = self.base_url + "getMe"
        r = self._request.get(url)
        return json.loads(r.content)

    """
    Method to receive incoming updates using long polling.
    An Array of Update objects is returned.

    kwargs:

    offset: int, optional (Defaults:100)
    Identifier of the first update to be returned. 
    Must be greater by one than the highest among the identifiers of previously received updates. 
    By default, updates starting with the earliest unconfirmed update are returned.

    limit: int, optional (Defaults:100)
    Limits the number of updates to be retrieved. Values between 1—100 are accepted

    timeout int, optional (Defaults:100)
    Timeout in seconds for long polling.

    allowed_updates, array of string optional [“message”, “edited_channel_post”, “callback_query”] (Defaults:all)
    List the types of updates you want your bot to receive.

    """
    def get_updates(self, **kwargs):
        offset = kwargs.get("offset", None)
        limit = kwargs.get("limit", None)
        timeout = kwargs.get("timeout", 100)
        allowed_updates = kwargs.get("allowed_updates", None)

        url = self.base_url + "getUpdates?"
        
        if offset is not None:
            url = url + "&offset={}".format(offset + 1)
        if limit is not None:
            url = url + "&limit={}".format(limit)
        if timeout is not None:
            url = url + "&timeout={}".format(timeout)
        if allowed_updates is not None:
            url = url + "&allowed_updates={}".format(allowed_updates)

        r = self._request.get(url)
        return json.loads(r.content)


    """
    Method to send a text message.

    kwargs:

    chat_id: Integer or String, REQUIRED
    Unique identifier for the target chat or username of the target channel 

    text: int, REQUIRED
    Text of the message to be sent

    parse_mode: String, optional
    Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.

    disable_web_page_preview: Boolean, optional
    Disables link previews for links in this message

    disable_notification: Boolean, optional
    Users will receive a notification with no sound.

    reply_to_message_id: Integer, optional
    If the message is a reply, ID of the original message

    reply_markup: Custom Formatting, optional
    Additional interface options. 
    A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

    """
    def send_message(self, chat_id, text, **kwargs):
        parse_mode = kwargs.get("parse_mode", None)
        disable_web_page_preview = kwargs.get("disable_web_page_preview", None)
        disable_notification = kwargs.get("disable_notification", None)
        reply_to_message_id = kwargs.get("reply_to_message_id", None)
        reply_markup = kwargs.get("reply_markup", None)
        timeout = kwargs.get("timeout", None)

        url = self.base_url + "sendMessage?chat_id={}&text={}".format(chat_id, text)

        if parse_mode is not None:
            url = url + "&parse_mode={}".format(parse_mode)
        if disable_web_page_preview is not None:
            url = url + "&disable_web_page_preview={}".format(disable_web_page_preview)
        if disable_notification is not None:
            url = url + "&disable_notification={}".format(disable_notification)
        if reply_to_message_id is not None:
            url = url + "&reply_to_message_id={}".format(reply_to_message_id)
        if reply_markup is not None:
            url = url + "&reply_markup={}".format(reply_markup)
        if timeout is not None:
            url = url + "&timeout={}".format(timeout)

        if text is not None:
            self._request.get(url)


    """
    Method to send a text message.

    kwargs:

    chat_id: Integer or String, REQUIRED
    Unique identifier for the target chat or username of the target channel 

    photo: int, REQUIRED
    Photo of the message to be sent, as string for the id and url, as multipart/form-data .post for file

    caption: Boolean, optional
    Photo caption (may also be used when resending photos by file_id), 0-1024 characters

    parse_mode: String, optional
    Send Markdown or HTML, if you want Telegram apps to show bold, italic, fixed-width text or inline URLs in your bot's message.

    disable_notification: Boolean, optional
    Users will receive a notification with no sound.

    reply_to_message_id: Integer, optional
    If the message is a reply, ID of the original message

    reply_markup: Custom Formatting, optional
    Additional interface options. 
    A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.

    """
    def send_photo(self, chat_id, photo, **kwargs):
        caption = kwargs.get("caption", None)
        parse_mode = kwargs.get("parse_mode", None)
        disable_notification = kwargs.get("disable_notification", None)
        reply_to_message_id = kwargs.get("reply_to_message_id", None)
        reply_markup = kwargs.get("reply_markup", None)
        timeout = kwargs.get("timeout", None)

        url = self.base_url + "sendMessage?chat_id={}&text={}".format(photo, chat_id)

        if caption is not None:
            url = url + "&caption={}".format(caption)
        if parse_mode is not None:
            url = url + "&parse_mode={}".format(parse_mode)
        if disable_notification is not None:
            url = url + "&disable_notification={}".format(disable_notification)
        if reply_to_message_id is not None:
            url = url + "&reply_to_message_id={}".format(reply_to_message_id)
        if reply_markup is not None:
            url = url + "&reply_markup={}".format(reply_markup)
        if timeout is not None:
            url = url + "&timeout={}".format(timeout)

        if photo is not None:
            self._request.get(url)