import telegram
import json
import configparser as cfg
from time import sleep


def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get("creds", "beta_token")


def make_reply(msg):
    reply = None
    if msg is None:
        return reply
    _msg = str(msg).upper()
    if _msg == "PT":
        reply = _msg
    return reply


update_id = None


def main():
    """
    Run the bot.
    """
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot(read_token_from_config_file("token.cfg"))

    while True:
        updates = bot.get_updates(offset=update_id)
        updates = updates["result"]
        if updates:
            for item in updates:
                update_id = item["update_id"]
                try:
                    message = str(item["message"]["text"])
                except:
                    message = None
                _chat = item["message"]["chat"]["id"]
                _user = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, _chat)
                bot.send_message(reply, _user)


#     try:
#         update_id = bot.get_updates()
#     except IndexError:
#         update_id = None
    
#     while True:
#         try:
#             echo(bot)
#         except:
#             sleep(1)


# def echo(bot):
#     """Echo the message the user sent."""
#     global update_id
#     # Request updates after the last update_id
#     for update in bot.get_updates(offset=update_id, timeout=10):
#         update_id = update.update_id + 1

#         if update.message:  # your bot can receive updates without messages
#             # Reply to the message
#             update.message.reply_text(update.message.text)


if __name__ == '__main__':
    main()