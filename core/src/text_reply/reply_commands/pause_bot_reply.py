from core.src.settings import (
    ENABLED
)
from core.src.languages_handler import chose_language


def response(language, status):

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
