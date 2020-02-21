from pvlv_commando import text_selector


def response(language, prefix):

    text = text_selector(language, 'response')  # the language and the file name
    return text.replace('{p}', prefix)
