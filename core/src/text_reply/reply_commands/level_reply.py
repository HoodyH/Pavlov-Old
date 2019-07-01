from core.src.languages_handler import chose_language


def user_field(language, user_name):

    def eng(): return 'My {}'.format(user_name)
    def ita(): return 'Mio {}'.format(user_name)

    return chose_language(
        language,
        eng, ita=ita
    )


def text_description(language, level):

    def eng(): return 'I\'m very proud of you\nYou are at level {}, keep up\ncompanion!'.format(level)
    def ita(): return 'Sono veramente fiero di te\nSei al livello {}, continua così\nCompagno!'.format(level)

    return chose_language(
        language,
        eng, ita=ita
    )

def text_description_global(language, level):

    def eng(): return 'I\'m very proud of you\nYou are at GLOBAL level {}, keep up\ncompanion!'.format(level)
    def ita(): return 'Sono veramente fiero di te\nSei al livello GLOBALE {}, continua così\nCompagno!'.format(level)

    return chose_language(
        language,
        eng, ita=ita
    )
