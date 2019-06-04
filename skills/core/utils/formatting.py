from skills.core.settings import *
from datetime import datetime



def from_timestamp(unixtime):
    """
    Args:
        unixtime (int):

    Returns:
        datetime.datetime:

    """
    if not unixtime:
        return None

    return datetime.fromtimestamp(unixtime)


def time_now():
    t = datetime.now()
    return "{}-{}-{} {}:{}:{}".format(t.year, t.month, t.day, t.hour, t.minute, t.second)


def mode_to_name(mode):
    if mode is DISABLED_MODE:
        return "DISABLED MODE"
    elif mode is QUIET_MODE:
        return "QUIET MODE"
    elif mode is NORMAL_MODE:
        return "NORMAL MODE"
    elif mode is SPAM_MODE:
        return "SPAM MODE"
