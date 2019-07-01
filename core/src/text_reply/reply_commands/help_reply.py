from core.src.languages_handler import chose_language


def response(language, prefix):

    def eng(): return 'To see the active commands in this Guild use "{}man all"'.format(prefix)
    def ita(): return 'Per vedere i comandi attivi in questa Gilda usa "{}man all"'.format(prefix)

    return chose_language(
        language,
        eng, ita=ita
    )

