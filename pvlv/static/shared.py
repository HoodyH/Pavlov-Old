from pvlv_commando import Commando


com: Commando


def init():
    global com
    com = Commando('pvlv/commands/')


init()
