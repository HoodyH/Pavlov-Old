from core.src.settings import (
    ITA,
    ENABLED, DISABLED
)


# HELP
def help_response(language, prefix):
    if language == ITA:
        out = 'Per vedere i comandi attivi in questa Gilda usa "{}man commands"'
    else:
        out = 'To see the active commands in this Guild use "{}man commands"'
    return out.format(prefix)


########################################################################
# MAN
def man_title(language, command_name, invocation_word):

    invocations = ', '.join(invocation_word)
    if language == ITA:
        out = '**Comando: {}**\nQuesto comando può essere invocato tramite queste parole chiave: **{}**'
        return out.format(command_name, invocations)
    else:
        out = '**Command: {}**\nThis command can be called using this keywords: **{}**'
        return out.format(command_name, invocations)


# MAN
def man_description(language, description):

    if language == ITA:
        return '**Descrizione:**\n{}'.format(description)
    else:
        return '**Description:**\n{}'.format(description)


# MAN
def man_usage(language, usage):

    if language == ITA:
        return '**Esempio di utilizzo:**\n{}'.format(usage)
    else:
        return '**Example of use:**\n{}'.format(usage)


########################################################################
# MODULE STATUS
def not_a_module(language, module):
    if language == ITA:
        return "{} non è un modulo, il comando non ha effetto".format(module)
    else:  # auto fall back on english
        return "{} is not a module, command has no effect".format(module)


# MODULE STATUS
def no_action_taken(language):
    if language == ITA:
        return "Nulla è stato cambiato"
    else:  # auto fall back on english
        return "Nothing has been changed"


# MODULE STATUS
def mode_updated(language, status_name):
    if language == ITA:
        return "La modalità {} è **attiva**.".format(status_name.upper())
    else:  # auto fall back on english
        return "{} mode is **active**.".format(status_name.upper())


# MODULE STATUS
def activation_status_update(language, module_name, status):

    m_name = module_name.replace('_', ' ').upper()

    if status is ENABLED:
        if language is ITA:
            return "il modulo {} è stato **Attivato**.".format(m_name)
        else:  # auto fall back on english
            return "{} module has been **Activated**.".format(m_name)
    elif status is DISABLED:
        if language is ITA:
            return "il modulo {} è stato **Disattivato**.".format(m_name)
        else:  # auto fall back on english
            return "{} module has been **Deactivated**.".format(m_name)
    else:
        return "Error"
