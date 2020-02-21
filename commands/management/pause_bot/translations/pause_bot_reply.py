from pvlv.settings import (
    ENABLED
)
from pvlv_commando import language_selector


def response(language, status):

    def eng(): return 'I\'m back motherfuckers!' if status is ENABLED else 'Ok, i\'ll just watch'
    def ita(): return 'Sono tornato merdeeeh!' if status is ENABLED else 'Ok, mi limiterò ad osservare'

    return language_selector(
        language,
        eng, ita=ita
    )
