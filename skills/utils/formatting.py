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