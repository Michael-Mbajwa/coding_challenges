import itertools


# Not 100% effective
def smallest_palindrome(string):
    """
    This problem was asked by Quora.

    Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible
    anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the
    lexicographically earliest one (the first one alphabetically).

    For example, given the string "race", you should return "ecarace", since we can add three letters to it
    (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made
    from "race" by adding three letters, but "ecarace" comes first alphabetically.

    As another example, given the string "google", you should return "elgoogle".
    :param string:
    :return:
    """
    palindromes = []
    string = string.lower()
    comb = [sorted(string)]
    for i in range(2, len(string)+1):
        temp = []
        for tup in itertools.permutations(string, i):
            temp.append("".join(tup))
        comb.append(sorted(temp))
    for sub_lst in comb:
        for char in sub_lst:
            for j in range(len(string)+1):
                if j == 0:
                    test = char + string
                    if test[:] == test[::-1]:
                        palindromes.append(test)
                elif j == len(string):
                    test = string + char
                    if test[:] == test[::-1]:
                        palindromes.append(test)
                else:
                    test = string[0:j] + char + string[j:]
                    if test[:] == test[::-1]:
                        palindromes.append(test)

    return sorted(palindromes)


if __name__ == "__main__":
    print(smallest_palindrome("race"))