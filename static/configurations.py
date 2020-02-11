import configparser as cfg
import logging


CONFIG_PATH = 'configs/pavlov.cfg'

parser = cfg.ConfigParser()
try:
    parser.read(CONFIG_PATH)
except Exception as exc:
    print(exc)

__beta = bool(parser.get('credentials', 'BETA'))
__TELEGRAM_TOKEN = parser.get('credentials', 'TELEGRAM_TOKEN_BETA', fallback='')
__TELEGRAM_TOKEN_BETA = parser.get('credentials', 'TELEGRAM_TOKEN', fallback='')
TOKEN = __TELEGRAM_TOKEN_BETA if __beta else __TELEGRAM_TOKEN

OWNER_ID = parser.get('admin', 'OWNER_ID', fallback=111111111)
LOGGING_CHAT = parser.get('admin', 'LOGGING_CHAT', fallback=111111111)

DEBUG = parser.get('debug', 'DEBUG', fallback=False)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pavlov')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)
