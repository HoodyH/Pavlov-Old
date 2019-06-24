from core.src.settings import (
    ITA, ENG,
    ENABLED, DISABLED
)


########################################################################
# HELP
def help_response(language, prefix):
    if language == ITA:
        out = 'Per vedere i comandi attivi in questa Gilda usa "{}man all"'
    else:
        out = 'To see the active commands in this Guild use "{}man all"'
    return out.format(prefix)


########################################################################
# MAN
def man_invocation(language, invocation_word):

    invocations = ', '.join(invocation_word)

    def ita(): return '**Invocazioni Alternative:**\n**{}**'.format(invocations)

    def eng(): return '**Alternative Invocations:**\n**{}**'.format(invocations)

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()


# MAN
def man_handled_args(language):

    def ita():
        return 'Argomenti Gestiti:'

    def eng():
        return 'Handled Arguments:'

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()


# MAN
def man_handled_params(language):
    def ita():
        return 'Parametri Gestiti:'

    def eng():
        return 'Handled Parameters:'

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()


def man_command_mask(language, prefix, main_command, sub_call):

    main_command = main_command.replace('_', '.')

    def ita():
        out = '**Comando abbreviato**\nOttenuto dal comando {}{}\nIn sostituzione a **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    def eng():
        out = '**Shortcut command**\nObtained from command {}{}\nIn substitution of **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()


########################################################################
# BOT PAUSE
def pause_response(language, status):
    if status is ENABLED:
        if language == ITA:
            return 'Il bot in pausa'
        else:
            return 'Bot has been paused'
    elif status is DISABLED:
        if language is ITA:
            return 'Sono sveglio!'
        else:
            return 'I am awake!'
    else:
        return "Error"


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
