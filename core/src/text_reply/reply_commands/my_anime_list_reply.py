from core.src.languages_handler import chose_language


def airing(language, on_airing, broadcast, premiered):

    def build_sentence(out_airing, out_completed):
        if on_airing:
            return '**{} {}**\n\n'.format(out_airing, broadcast)
        else:
            return '{} {}\n\n'.format(out_completed, premiered)

    def eng():
        out_airing = 'Airing on'
        out_completed = '**Status:** Completed\n**Premiered on:**'
        return build_sentence(out_airing, out_completed)

    def ita():
        out_airing = 'Prossimo ep'
        out_completed = '**Stato:** Completato\n**Prima uscita:**'
        return build_sentence(out_airing, out_completed)

    return chose_language(
        language,
        eng, ita=ita
    )


def genres(language, gens):

    gens = gens[:5]

    def build_list():
        out = ''
        for genre in gens:
            out += '{}, '.format(genre)
        out = out[:-2]
        out += '\n'
        return out

    def eng(): return '**Genre:** {}'.format(build_list())
    def ita(): return '**Genere:** {}'.format(build_list())

    return chose_language(
        language,
        eng, ita=ita
    )


def details(language, episodes, duration, rank, score,):

    def build_sentence(sentence):
        return sentence.format(
            episodes,
            duration,
            rank,
            score,
        )

    def eng(): return build_sentence('**Episodes:** {}\n**Ep duration:** {}\n**Rank:** {}\n**Score:** {}\n')
    def ita(): return build_sentence('**Episodi:** {}\n**Durata ep:** {}\n**Rank:** {}\n**Voto:** {}\n')

    return chose_language(
        language,
        eng, ita=ita
    )


def no_arg_error(language):

    def eng(): return 'You have to provide an argument to be able to execute the search'
    def ita(): return 'Necessaria un parola chiave come argomento per eseguire la ricerca'

    return chose_language(
        language,
        eng, ita=ita
    )

