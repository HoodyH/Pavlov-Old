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


DEBUG = parser.get('debug', 'DEBUG', fallback=False)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pavlov')

if DEBUG:
    logger.setLevel(logging.INFO)
else:
    logger.setLevel(logging.ERROR)
