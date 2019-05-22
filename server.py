import telegram

import json
import configparser as cfg

from skills.skills import Analyze

update_id = None
bot_id_0 = ""
bot_id_1 = ""

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    bot_id_0 = parser.get("creds", "bot_id_0")
    bot_id_1 = parser.get("creds", "bot_id_1")
    return parser.get("creds", "beta_token")


def do_stuffs(msg):
    # if msg.user.id != bot_id_0 and msg.user.id != bot_id_1:
        if msg.text is None:
            return
        if msg.chat is not None:
            c = Analyze("telegram", msg.chat.id, msg.user.id)  
        else:
            c = Analyze("telegram", None, msg.user.id) 
        r = c.analyze_message(msg.text)
        if r is not None:
            msg.send_text(r)
        return


def main():
    """Run the bot."""
    global update_id
    bot = telegram.Bot(read_token_from_config_file("token.cfg"))
    msg = telegram.Message(bot) #super obj

    while True:
        incoming_data = bot.get_updates(offset=update_id)
        incoming_data = incoming_data["result"]
        if incoming_data:
            for item in incoming_data:
                update_id = item["update_id"]
                msg.extract_data(item)
                do_stuffs(msg)


if __name__ == '__main__':
    main()