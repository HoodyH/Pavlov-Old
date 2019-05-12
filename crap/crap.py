import json
import configparser as cfg

def read_token_from_config_file(config):
    parser = cfg.ConfigParser()
    parser.read(config)
    return parser.get("creds", "beta_token")

def make_reply(msg):
    reply = None
    if msg is None:
        return reply
    _msg = str(msg).upper()
    if _msg == "PT":
        reply = _msg
    return reply