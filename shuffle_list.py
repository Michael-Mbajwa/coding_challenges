import random


def shuffle_method(sequence):
    """Python’s random module includes a function shuffle(data) that accepts a list of elements
    and randomly reorders the elements so that each possi- ble order occurs with equal probability.
    The random module includes a more basic function randint(a, b) that returns a uniformly
    random integer from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function."""
    sequence_copy = sequence[:]
    reshuffled_list = []
    length_sequence = len(sequence_copy)

    while sequence_copy:
        if length_sequence == 1:
            value = sequence_copy[0]
            reshuffled_list.append(value)
            del sequence_copy[0]
            length_sequence -= 1

        else:
            rand_int = random.randint(0, (length_sequence - 1))
            new_value = sequence_copy[rand_int]
            reshuffled_list.append(new_value)
            del sequence_copy[rand_int]
            length_sequence -= 1

    return reshuffled_list


print(shuffle_method([2, 4, 5, 7, 9, 10, 23]))