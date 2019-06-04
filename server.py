import telegram
from skills.skills import Analyze
from skills.core.settings import *


update_id = None


def do_stuffs(msg):
    if msg.text is None:
        return
    if msg.chat is not None:
        c = Analyze("telegram", msg.chat.id, msg.chat.title, msg.from_user.id, msg.from_user.username)
    else:
        c = Analyze("telegram", None, None, msg.from_user.id, msg.from_user.username)

    return c.analyze_message(msg.text)


def main():
    """Run the bot."""
    global update_id
    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me().first_name)

    while True:
        updates = bot.get_updates(offset=update_id)
        for u in updates:
            update_id = u.update_id + 1
            try:
                r = do_stuffs(u.message)
                if r is not None:
                    bot.send_message(chat_id=u.message.chat.id, text=r)
            except Exception as e:
                pass


if __name__ == '__main__':
    main()
