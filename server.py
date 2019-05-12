import logging
import telegram
from time import sleep

import json
import configparser as cfg

from skills.simply_respond import respond

update_id = None
bot_id_0 = ""
bot_id_1 = ""

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    bot_id_0 = parser.get("creds", "bot_id_0")
    bot_id_1 = parser.get("creds", "bot_id_1")
    return parser.get("creds", "stable_token")

def main():
    """Run the bot."""
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
                
                print(message)

                if _user != bot_id_0 and _user != bot_id_1:
                    r = respond(message)
                    if r is not None:
                        bot.send_message(r, _chat)


if __name__ == '__main__':
    main()