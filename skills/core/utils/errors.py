from skills.core.settings import *


def command_error(language):
    if language is ITA:
        return "Questo non è un comando."
    else:  # auto fall back on english
        return "This is not a command."


def parse_error(language, argument, suggestion):
    if language is ITA:
        return "The {} value is not valid.\nTry something like {}".format(argument, suggestion)
    else:  # auto fall back on english
        return "Il valore di {} non è valido.\nProva ad usare {}".format(argument, suggestion)


def command_not_implemented(language):
    if language is ITA:
        return "Questo comando non è ancora stato implementato."
    else:  # auto fall back on english
        return "This is not implemented jet."


