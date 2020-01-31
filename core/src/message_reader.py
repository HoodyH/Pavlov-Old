

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


def _clean():
    """
    clean article and conjunctions0
    clean gender
    clean repetitions
        (letters repetitions,
        modules repetitions (leave just 2 near) hahahaha will become haha,
        words repetiotion (in the same trigger)

    different order: (be output_permission)
    in check sequence the trigger array can have the same words of in a different order

    percentage match: (be output_permission)
    some word can be omitted, but you must have 70% of the words

    example:
    trigger:
    hello madaffacca how is going

    elaboration:
    helo madafaca how is going

    input: (must be saved end elaborated once)
    madafacca how is going
    """
    return
