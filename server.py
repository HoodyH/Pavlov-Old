import telegram
from skills.skills import Analyze
from skills.core.settings import *


update_id = None


def do_stuffs(msg):
    if msg.text is None:
        return
    if msg.chat is not None:
        c = Analyze("telegram", msg.chat.id, msg.chat.title, msg.user.id, msg.user.username)
    else:
        c = Analyze("telegram", None, None, msg.user.id, msg.user.username)

    r = c.analyze_message(msg.text)
    if r is not None:
        msg.send_text(r)
    return


def main():
    """Run the bot."""
    global update_id
    bot = telegram.Bot(TOKEN)
    msg = telegram.Message(bot)  # super obj

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
