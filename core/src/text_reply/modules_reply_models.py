from core.src.settings import (
    ITA,
    ENABLED, DISABLED
)


# MODULE CONFIG
def not_a_module(language, module):
    if language is ITA:
        return "{} non è un modulo, il comando non ha effetto".format(module)
    else:  # auto fall back on english
        return "{} is not a module, command has no effect".format(module)


# MODULE CONFIG
def no_action_taken(language):
    if language is ITA:
        return "Nulla è stato cambiato"
    else:  # auto fall back on english
        return "Nothing has been changed"


# MODULE CONFIG
def mode_updated(language, status_name):
    if language is ITA:
        return "La modalità {} è attiva.".format(status_name.upper())
    else:  # auto fall back on english
        return "{} module_mode is active.".format(status_name.upper())


# MODULE CONFIG
def activation_status_update(language, module_name, status):
    if status is ENABLED:
        if language is ITA:
            return "il modulo {} è stato Attivato.".format(module_name.upper())
        else:  # auto fall back on english
            return "{} module has been Activated.".format(module_name.upper())
    elif status is DISABLED:
        if language is ITA:
            return "il modulo {} è stato Disattivato.".format(module_name.upper())
        else:  # auto fall back on english
            return "{} module has been Deactivated.".format(module_name.upper())
    else:
        return "Error"


