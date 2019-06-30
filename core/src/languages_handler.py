from core.src.settings import (
    ITA, ENG,
)


def chose_language(language, eng, ita=None):

    languages = {
        ITA: ita,
        ENG: eng
    }

    try:
        return languages[language]()
    except Exception as e:
        print(e)
        return languages[ENG]()
