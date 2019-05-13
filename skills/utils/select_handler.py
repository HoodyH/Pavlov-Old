import random

def random_between(min, max):

    if min == max:
        return min

    return int(random.random() * (max - min) + min)