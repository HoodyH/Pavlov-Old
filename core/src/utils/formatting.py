from core.src.settings import *
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


def remap_range(value, actual_min, actual_max, new_min, new_max):
    actual_span = actual_max - actual_min
    new_span = new_max - new_min
    value_scaled = float(value - actual_min) / float(actual_span)
    return int(new_min + (value_scaled * new_span))


"""
    +-----------------------------------------+
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+         |
    |                                         | span    |
    |             SPAN_TOP_TITLE              | span    |SPAN_TITLE_SECTION
    |                                         | span    |
    +-----------------------------------------+         |
    |             SPAN_BORDER                 | span    |
    +-----------------------------------------+                
    |             SPAN_GRAPH_TITLE            | span                
    |                                         | span                
    +-----------------------------------------+                     
    |             SPAN_GRAPH_SUBTITLE         | span    |           
    +--+-----------------------------------+--+         |              
    |  |          GRAPH_BORDER             |  | span    |           
    |--+-----------------------------------+--|         |           
    |  |                                   |  | span    |           
    |  |          GRAPH                    |  | span    |SPAN_GRAPH 
    |  |                                   |  | span    |           
    |  |                                   |  | span    |           
    |--+-----------------------------------+--|         |           
    |  |          GRAPH_BORDER             |  | span    |           
    +--+-----------------------------------+--+                                         
    |                                         | span                
    |             SPAN_GRAPH_TEXT             | span                
    |                                         | span        
    |                                         | span                
    +-----------------------------------------+
    |             SPAN_BORDER                 | span  
    +-----------------------------------------+                    


"""