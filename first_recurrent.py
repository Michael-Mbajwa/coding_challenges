from collections import defaultdict


def first_recurrent(string):
    """
    This problem was asked by Google.

    Given a string, return the first recurring character in it, or null if there is no recurring character.

    For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
    :return:
    """
    count = defaultdict(int)
    for char in string:
        if count[char]:
            return char
        else:
            count[char] += 1
    return "Null"


if __name__ == "__main__":
    print(first_recurrent("acbbac"))