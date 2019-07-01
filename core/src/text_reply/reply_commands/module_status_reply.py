from core.src.settings import (
    ENABLED, DISABLED
)
from core.src.languages_handler import chose_language


def not_a_module(language, module):

    def eng(): return '{} is not a module, command has no effect'.format(module)
    def ita(): return '{} non è un modulo, il comando non ha effetto'.format(module)

    return chose_language(
        language,
        eng, ita=ita
    )


def no_action_taken(language):

    def eng(): return 'Nothing has been changed'
    def ita(): return 'Nulla è stato cambiato'

    return chose_language(
        language,
        eng, ita=ita
    )


def mode_updated(language, status_name):

    def eng(): return '{} mode is **active**.'.format(status_name.upper())
    def ita(): return 'La modalità {} è **attiva**.'.format(status_name.upper())

    return chose_language(
        language,
        eng, ita=ita
    )


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
