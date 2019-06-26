from core.src.settings import (
    ITA,
    STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE
)
from core.src.text_reply.languages_handler import chose_language


def guild_not_pro(language):

    def eng(): return 'This guild has not the right pro status to run this command.'
    def ita(): return 'Questa gilda non ha un pro status sufficiente per eseguire quest comando.'

    return chose_language(
        language,
        eng, ita=ita
    )


def command_error(language):

    def eng(): return 'This is not a command.'
    def ita(): return 'Questo non è un comando.'

    return chose_language(
        language,
        eng, ita=ita
    )


def command_not_implemented(language):

    def eng(): return 'This is not implemented jet.'
    def ita(): return 'Questo comando non è ancora stato implementato.'

    return chose_language(
        language,
        eng, ita=ita
    )


def parse_error(language, argument, suggestion):

    def eng(): return 'The value: "{}" is not valid.\nTry something like "{}"'.format(argument, suggestion)
    def ita(): return 'Il valore: "{}" non è valido.\nProva ad usare "{}"'.format(argument, suggestion)

    return chose_language(
        language,
        eng, ita=ita
    )


WRONG_STATIC_MODE_STRING = 1


def message_reply_error(language, error_type, trigger=None):

    def eng():
        if error_type is WRONG_STATIC_MODE_STRING:
            return 'Wrong syntax in trigger {}\nSTATIC_OVERRIDE_MODE: {}{}{}\nSTATIC_SPAM_MODE: {}{}{}'.format(
                trigger,
                STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE, STATIC_SPLIT_MODE,
                STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE, STATIC_SPLIT_MODE
            )

    def ita():
        if error_type is WRONG_STATIC_MODE_STRING:
            return 'Sintassi errata nel trigger: {}\nSTATIC_OVERRIDE_MODE: {}{}{}\nSTATIC_SPAM_MODE: {}{}{}'.format(
                trigger,
                STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE, STATIC_SPLIT_MODE,
                STATIC_SPLIT_MODE, STATIC_OVERRIDE_MODE, STATIC_SPLIT_MODE
            )

    return chose_language(
        language,
        eng, ita=ita
    )


def arg_not_found_error(language):

    def eng(): return 'The argument of this command is wrong or not existent.'
    def ita(): return 'L\'argomento di questo comando è errato o inesistente.'

    return chose_language(
        language,
        eng, ita=ita
    )




