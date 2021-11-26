import random


def my_choice(seq):
    """Using only the randrange function, implement your own version of the choice function."""
    len_seq = len(seq)
    i = random.randrange(len_seq)
    result = seq[i]
    return result
