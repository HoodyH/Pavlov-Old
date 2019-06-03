import configparser as cfg
parser = cfg.ConfigParser()
parser.read("token.cfg")
MONGO_DB_CONNECTION_STRING = parser.get("creds", "mongo_connection_string")
TOKEN = parser.get("creds", "token")
# API
from API.badass_character.badass_character import BadassCharacter
badass_character = BadassCharacter()
from API.bestemmia.bestemmia import Bestemmia
bestemmia = Bestemmia()
from API.pickup_line.pickup_line import PickupLine
pickup_line = PickupLine()
# database
from skills.core.db.database import DB
db = DB('mongodb+srv://MainUserBot:AdminDb12@abot-3jqai.mongodb.net/test?retryWrites=true')


ERROR = -1
# debug
USE_GLOBAL_FILE_ONLY = True


# Languages Handled for messages
ITA = 'ita'
ENG = 'eng'


# message max length for analyze
MEX_MAX_LENGTH = 70


# situational reply settings
AVOID_REPLY = 0
STD_REPLAY = 1
POWER_REPLAY = 2
STATIC_REPLAY = 3
STATIC_SPLIT_KEY = '&&&'
STATIC_SPLIT_MODE = '%%%'
STATIC_OVERRIDE_MODE = '!'


# CONFIGURATION SETTINGS
# prefix type
NO_PREFIX = -1
COMMAND_PREFIX = 0
OVERRIDE_PREFIX = 1
SUDO_PREFIX = 2

# global setting for auto reply commands
DISABLED_MODE = -1
QUIET_MODE = 0
NORMAL_MODE = 1
SPAM_MODE = 2
AGGRESSIVE_MODE = 3

# module type, to define the scope of the module
TYPE_LISTENER = 0
TYPE_COMMAND = 1


# ERRORS CONFIG
# message_reply_error
WRONG_STATIC_MODE_STRING = 1
