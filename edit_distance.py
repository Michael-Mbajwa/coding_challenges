def edit_distance(str1, str2):
    """
    This problem was asked by Google.

    The edit distance between two strings refers to the minimum number of character insertions, deletions,
    and substitutions required to change one string to the other. For example, the edit distance between “kitten” and
    “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

    Given two strings, compute the edit distance between them.
    :return:
    """
    if type(str1) == str and type(str2) == str:
        # for this code, I am considering uppercase as different from lowercase. This means 'K' is different from 'k'
        edits_count = 0
        if str1 == str2:
            return 0
        if len(str1) != len(str2):
            # If the strings are not of the same length, we know we have to make edits
            # equal to differences of the two strings
            edits_count += (max(len(str1), len(str2)) - min(len(str1), len(str2)))
        # Zip compares the characters of the two strings up to the length of the shortest
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                edits_count += 1

        return edits_count
    return "Only strings permitted"


if __name__ == "__main__":
    result = edit_distance(str1="Kitten", str2="sitting")
    print(result)