def shifted_strings(A, B):
    """
    This problem was asked by Google.

    Given two strings A and B, return whether or not A can be shifted some number of times to get B.

    For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
    :return: True or False
    :param A: string 1
    :param B: string 2
    """
    # I won't necessarily the code is naive but the worst case time complexity is O(n).
    shift = A[1:] + A[0]  # Perform the first shift
    while shift != A:  # We will keep shifting until we reach the starting point of A.
        if shift == B:
            return True  # if the shifting result to B, program terminates
        else:
            shift = shift[1:] + shift[0]  # Perform next shift

    return False  # If no shift results to B, code returns False


if __name__ == "__main__":
    print(shifted_strings('abc', 'acb'))