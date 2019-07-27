from telegram_bot import TelegramBot
from core.starter import Starter
import configparser as cfg
from core.src.static_modules import (telegram_bot_abstraction)
from core.secret_agency.agent_manager import Agency

parser = cfg.ConfigParser()
parser.read("token.cfg")
MONGO_DB_CONNECTION_STRING = parser.get("creds", "mongo_connection_string")
TELEGRAM_TOKEN = parser.get("creds", "token")
MAIN_AGENT_TOKEN = parser.get("creds", "telegram_secret_agent")


def main():

    agency = Agency()
    agency.run([MAIN_AGENT_TOKEN])

    # all the main obj that last for all the time that the bot run must be created on this level
    telegram_starter = Starter(telegram_bot_abstraction)
    telegram_bot = TelegramBot(TELEGRAM_TOKEN, telegram_starter)
    telegram_bot.run()


if __name__ == '__main__':

    print(
        "\n +--------------------------------------------+"
        "\n |          AbbestiaDC - Bot Manager          |"
        "\n |            (c) 2019 AbbestiaDC             |"
        "\n +--------------------------------------------+\n\n"
    )

    main()
