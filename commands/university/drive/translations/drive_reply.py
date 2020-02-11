from old_core.src.languages_handler import chose_language


def void_folder(language, arg):

    def eng():
        out = 'La cartella {} non ha contenuti\n'.format(arg)
        out += '\n**.uni**\nPer vedere l\'elenco dei corsi.'.format(arg)
        return out

    def ita():
        out = 'La cartella {} non ha contenuti\n'.format(arg)
        out += '\n**.uni**\nPer vedere l\'elenco dei corsi.'.format(arg)
        return out

    return chose_language(
        language,
        eng, ita=ita
    )
