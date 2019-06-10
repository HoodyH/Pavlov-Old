from telegram_bot import TelegramBot
import configparser as cfg

parser = cfg.ConfigParser()
parser.read("token.cfg")
MONGO_DB_CONNECTION_STRING = parser.get("creds", "mongo_connection_string")
TELEGRAM_TOKEN = parser.get("creds", "token")


def main():
    telegram_bot = TelegramBot(TELEGRAM_TOKEN)
    telegram_bot.run()


if __name__ == '__main__':
    main()
