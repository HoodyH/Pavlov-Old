import random

CHUCK_NORRIS = "chuck_norris"
JOHN_WICK = "john_wick"

supported_character = [
    CHUCK_NORRIS,
    JOHN_WICK
]

supported_languages = [
    "ita",
    "eng"
]


class BadassCharacter(object):
    """

    """
    def __init__(self, folder_path):

        self.folder_path = folder_path
        self.chuck_norris_ENG = []
        self.chuck_norris_ITA = []
        self.john_wick_ENG = []
        self.john_wick_ITA = []
        self._load_data()

        self.output = []

    def _load_data(self):
        filename = self.folder_path + '/badass_character/ITA/john_wick.txt'

        line_counter = 0
        with open(filename) as file:
            for line in file:
                line_counter += 1
                self.john_wick_ITA.append([line_counter, line])
                self.john_wick_ENG.append([line_counter, line])

        filename = self.folder_path + '/badass_character/ENG/chuck_norris.txt'

        line_counter = 0
        with open(filename) as file:
            for line in file:
                line_counter += 1
                self.chuck_norris_ITA.append([line_counter, line])
                self.chuck_norris_ENG.append([line_counter, line])

    @staticmethod
    def _random_between(n_min, n_max):

        if n_min == n_max:
            return n_min

        return int(random.random() * (n_max - n_min) + n_min)

    def badass_sentence(self, language, character, number=None):

        sentences_vector = getattr(self, '{}_{}'.format(character, language.upper()))

        if number is None:
            sentence_number = self._random_between(0, len(sentences_vector)-1)
        else:
            sentence_number = number - 1

        output = '{} - {}:\n'.format(" ".join(character.split('_')).upper(), sentence_number + 1)
        output += sentences_vector[sentence_number][1]

        return output


