import random

MALE = 1
FEMALE = 2

supported_default = {
    'eng': {
        'gender': 0,
        'characters': {
            'god': 1,
            'madonna': 2,
            'gesu': 1,
            'allah': 1,
            'whore': 2
        }
    },
    'ita': {
        'gender': 1,
        'male': 'o',
        'female': 'a',
        'characters': {
            'dio': 1,
            'madonna': 2,
            'gesù': 1,
            'allah': 1,
            'troia': 2,
            'puttana': 2
        }

    }
}


class Bestemmia(object):
    """

    """
    def __init__(self):

        self._load_data()

    def _load_data(self):

        for language in supported_default.keys():
            filename = 'API/bestemmia/{}/bestemmia_sentences_base.txt'.format(language.upper())
            line_counter = 0
            var_valor = []
            with open(filename) as file:
                for line in file:
                    line_counter += 1
                    var_valor.append(line)
                var_name = 'bestemmia_sentences_base_{}'.format(language.upper())
                setattr(self, var_name, var_valor)

    @staticmethod
    def _random_between(n_min, n_max):

        if n_min == n_max:
            return n_min

        return int(random.random() * (n_max - n_min) + n_min)

    def bestemmia(self, language, character=None, gender=None):

        # load the right local variable
        sentences_vector = getattr(self, 'bestemmia_sentences_base_{}'.format(language.upper()))

        # generate sentence number
        sentence_number = self._random_between(0, len(sentences_vector)-1)


        # genarate a random response
        if character is None and gender is None:
            return ""

        # read the gender from the dictionary
        elif character is not None and gender is None:

            data_language = supported_default.get(language)
            # check if this field exist
            if data_language is None:
                return ""

            # check if the character exists in the dictionary
            characters = data_language.get('characters')
            if character in characters.keys():
                # check if characters has gender variable
                gender_replacer = ''
                if data_language.get('gender') is 1:
                    # get the right gender replacer
                    if characters.get(character) is MALE:
                        gender_replacer = data_language.get('male')
                    elif characters.get(character) is FEMALE:
                        gender_replacer = data_language.get('female')
                    else:
                        return ""
                adder = sentences_vector[sentence_number].replace('%%%', gender_replacer)
                return '{} {}'.format(character.title(), adder)
            else:
                return ""

        # not handled
        else:
            return ""


