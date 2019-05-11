from t_wrapper import telegram_wrapper

bot = telegram_wrapper("token.cfg")


def make_reply(msg):
    reply = None
    if msg.upper() == "PT":
        reply = msg.upper()
    return reply


def main():
    update_id = None
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
                from_ = item["message"]["from"]["id"]
                reply = make_reply(message)
                bot.send_message(reply, from_)

main()