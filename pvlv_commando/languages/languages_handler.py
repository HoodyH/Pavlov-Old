from pvlv.settings import (
    ITA, ENG,
)


def language_selector(language, eng, ita=None):

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()
