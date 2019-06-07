

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

    different order: (be disabled)
    in check sequence the trigger array can have the same words of in a different order

    percentage match: (be disabled)
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


# command parameter reader
def _extract_value(input_array, starting_point=0):

    val = ""
    for j in range(starting_point, len(input_array)):
        # if is a input string
        if str.startswith(input_array[j], '-'):
            break
        if str.startswith(input_array[j], '"'):
            val += "{} ".format(input_array[j][1:])
        elif str.endswith(input_array[j], '"'):
            val += "{} ".format(input_array[j][:-1])
            break
        else:
            val += "{} ".format(input_array[j])
    if str.endswith(val, ' '):
        return val[:-1]
    else:
        return val


def extract_command_parameters(text):
    """
    text must be a string or a list
    :return: argument as string, parameters as tuple [parameter, data]
    """
    if isinstance(text, list):
        text_array = text
    else:
        text_array = text.split()

    arg = ""
    params = []
    text_array.pop(0)  # remove the command trigger
    for i in range(0, len(text_array) - 1):
        if str.startswith(text_array[i], '-'):
            param_key = text_array[i][1:]
            param = [param_key]
            param_val = _extract_value(text_array, i + 1)
            param.append(param_val)
            params.append(param)
        elif i is 0:
            arg = _extract_value(text_array)
    return arg, params
