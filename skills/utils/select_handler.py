import random


def random_between(min, max):

    if min == max:
        return min

    return int(random.random() * (max - min) + min)


def phrase_sequencer(words_array, current_val):
    current_val += 1
    if current_val >= len(words_array):
        current_val = 0

    return current_val, words_array[current_val]
