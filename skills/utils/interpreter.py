

def find(to_find, find_in, starting_point=None):

    if to_find == "":
        return

    sample_array = to_find.upper().split()
    sentence_array = find_in.upper().split()

    if starting_point is None:
        # This loop look for that keyword il all the sentence
        for i in range(0, len(sentence_array)):
            if _find_sequence(sample_array, sentence_array, i):
                return True
        return False
    else:
        # This look for a specific sequence that must start from the given point or abort
        return _find_sequence(sample_array, sentence_array, starting_point)


def _find_sequence(sample_array, sentence_array, starting_point):

    for i in range(0, len(sample_array)):

        if starting_point + i > len(sentence_array) - 1:
            # if i'm at the end of the sentence then abort
            return False
        if sample_array[i].upper() != sentence_array[starting_point + i].upper():
            # if in the array a word dont match then abort
            return False
    return True
