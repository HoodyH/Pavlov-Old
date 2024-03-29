import random

CHUCK_NORRIS = "Chuck Norris"
JOHN_WICK = "John Wick"


supported_languages = [
    "eng",
    "ita"
]


class BadassCharacter(object):

    def __init__(self):

        self._load_data()

    def _load_data(self):

        for language in supported_languages:
            filename = 'API/badass_character/{}/badass_sentences.txt'.format(language.upper())
            var_valor = []
            with open(filename) as file:
                for line in file:
                    var_valor.append(line)
                var_name = 'badass_sentences_{}'.format(language.upper())
                setattr(self, var_name, var_valor)

    @staticmethod
    def _random_between(n_min, n_max):

        if n_min == n_max:
            return n_min

        return int(random.random() * (n_max - n_min) + n_min)

    def badass_sentence(self, language, character, number=None):

        sentences_vector = getattr(self, 'badass_sentences_{}'.format(language.upper()))

        if number is None:
            sentence_number = self._random_between(0, len(sentences_vector)-1)
        else:
            sentence_number = number - 1

        output = '{} - {}:\n'.format(character.upper(), sentence_number + 1)
        output += sentences_vector[sentence_number].replace('%%%', character.title())

        return output
