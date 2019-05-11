from t_wrapper import telegram_wrapper

bot = telegram_wrapper("token.cfg")


def make_reply(msg):
    reply = None
    if msg is None:
        return reply
    _msg = str(msg).upper()
    if _msg == "PT":
        reply = _msg
    return reply


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
            _chat = item["message"]["chat"]["id"]
            _user = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, _chat)
            bot.send_message(reply, _user)
