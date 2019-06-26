from core.src.settings import (
    ENABLED, DISABLED
)
from core.src.text_reply.languages_handler import chose_language


########################################################################
# HELP
def help_response(language, prefix):

    def eng(): return 'To see the active commands in this Guild use "{}man all"'.format(prefix)
    def ita(): return 'Per vedere i comandi attivi in questa Gilda usa "{}man all"'.format(prefix)

    return chose_language(
        language,
        eng, ita=ita
    )


########################################################################
# MAN
def man_invocation(language, invocation_word):

    invocations = ', '.join(invocation_word)

    def eng(): return '**Alternative Invocations:**\n**{}**'.format(invocations)
    def ita(): return '**Invocazioni Alternative:**\n**{}**'.format(invocations)

    return chose_language(
        language,
        eng, ita=ita
    )


# MAN
def man_handled_args(language):

    def eng(): return 'Handled Arguments:'
    def ita(): return 'Argomenti Gestiti:'

    return chose_language(
        language,
        eng, ita=ita
    )


# MAN
def man_handled_params(language):

    def eng(): return 'Handled Parameters:'
    def ita(): return 'Parametri Gestiti:'

    return chose_language(
        language,
        eng, ita=ita
    )


def man_command_mask(language, prefix, main_command, sub_call):

    main_command = main_command.replace('_', '.')

    def eng():
        out = '**Shortcut command**\nObtained from command {}{}\nIn substitution of **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    def ita():
        out = '**Comando abbreviato**\nOttenuto dal comando {}{}\nIn sostituzione a **{}{} {}**'.format(
            prefix, main_command,
            prefix, main_command, sub_call
        )
        return out

    return chose_language(
        language,
        eng, ita=ita
    )


########################################################################
# BOT PAUSE
def pause_response(language, status):

    def eng():
        if status is ENABLED:
            return 'I am awake!'
        else:
            return 'Bot has been paused'

    def ita():
        if status is ENABLED:
            return 'Sono sveglio!'
        else:
            return 'Il bot in pausa'

    return chose_language(
        language,
        eng, ita=ita
    )


########################################################################
# MODULE STATUS
def not_a_module(language, module):

    def eng(): return '{} is not a module, command has no effect'.format(module)
    def ita(): return '{} non è un modulo, il comando non ha effetto'.format(module)

    return chose_language(
        language,
        eng, ita=ita
    )


# MODULE STATUS
def no_action_taken(language):

    def eng(): return 'Nothing has been changed'
    def ita(): return 'Nulla è stato cambiato'

    return chose_language(
        language,
        eng, ita=ita
    )


# MODULE STATUS
def mode_updated(language, status_name):

    def eng(): return '{} mode is **active**.'.format(status_name.upper())
    def ita(): return 'La modalità {} è **attiva**.'.format(status_name.upper())

    return chose_language(
        language,
        eng, ita=ita
    )


# MODULE STATUS
def activation_status_update(language, module_name, status):

    m_name = module_name.replace('_', ' ').upper()

    def eng():
        if status is ENABLED:
            return '{} module has been **Activated**.'.format(m_name)
        elif status is DISABLED:
            return '{} module has been **Deactivated**.'.format(m_name)
        else:
            return 'Error'

    def ita():
        if status is ENABLED:
            return 'il modulo {} è stato **Attivato**.'.format(m_name)
        elif status is DISABLED:
            return 'il modulo {} è stato **Disattivato**.'.format(m_name)
        else:
            return 'Error'

    return chose_language(
        language,
        eng, ita=ita
    )
