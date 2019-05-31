from skills.core.settings import *


# MODULE CONFIG
def no_action_taken(language):
    if language is ITA:
        return "Nulla è stato cambiato"
    else:  # auto fall back on english
        return "Nothing has bBNen changed"


# MODULE CONFIG
def mode(language, status_name):
    if language is ITA:
        return "La modalità {} è attiva.".format(status_name.upper())
    else:  # auto fall back on english
        return "{} mode is active.".format(status_name.upper())


# MODULE CONFIG
def deactivation(language, module_name):
    if language is ITA:
        return "il modulo {} è stato attivato.".format(module_name.upper())
    else:  # auto fall back on english
        return "{} module has been deactivated.".format(module_name.upper())
