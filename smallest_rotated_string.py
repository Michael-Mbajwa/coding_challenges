def smallest_rotated_string(string, k):
    """
    You are given a string of length n and an integer k. The string can be manipulated by taking one of the first k
    letters and moving it to the end of the string.
    Write a program to determine the lexicographically smallest string that can be created after an unlimited number of
    moves.
    For example, suppose we are given the string daily and k = 1. The best we can create in this case is ailyd.
    :param string:
    :return:
    """
    # As long as we are allowed to move the first or second letter, we will always have a sorted string.
    if k > 1:
        return ''.join(sorted(string))
    elif k == 1:  # The algorithm keeps rotating the string until we get back to the original string
        best = string
        terminate = False
        temp_string = string
        while not terminate:
            temp_string = temp_string[1:] + temp_string[0]
            if temp_string < best:
                best = temp_string
            if string == temp_string:
                terminate = True
        return best


if __name__ == "__main__":
    print(smallest_rotated_string("daily", 2))