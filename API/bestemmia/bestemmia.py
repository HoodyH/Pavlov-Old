import random

MADONNA = "Madonna"
DIO = "Dio"

supported_languages = [
    "ita"
]

MALE = 1
FEMALE = 2


class Bestemmia(object):
    """

    """
    def __init__(self):

        self._load_data()

    def _load_data(self):

        for language in supported_languages:
            filename = 'API/bestemmia/{}/bestemmia_sentences_base.txt'.format(language.upper())
            line_counter = 0
            var_valor = []
            with open(filename) as file:
                for line in file:
                    line_counter += 1
                    var_valor.append([line_counter, line])
                var_name = 'bestemmia_sentences_base_{}'.format(language.upper())
                setattr(self, var_name, var_valor)

    @staticmethod
    def _random_between(n_min, n_max):

        if n_min == n_max:
            return n_min

        return int(random.random() * (n_max - n_min) + n_min)

    def bestemmia(self, language, character=None, gender=None, number=None):

        sentences_vector = getattr(self, 'bestemmia_sentences_base_{}'.format(language.upper()))

        if number is None:
            sentence_number = self._random_between(0, len(sentences_vector)-1)
        else:
            sentence_number = number - 1

        if language == 'ita':
            if gender is MALE:
                gender_replacer = 'o'
            elif gender is FEMALE:
                gender_replacer = 'a'
            else:
                return ''
            output = sentences_vector[sentence_number][1].replace('%%%', gender_replacer)

        return output
