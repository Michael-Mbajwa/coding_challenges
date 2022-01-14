def perfect_digit(n):
    """
    This problem was asked by Microsoft.

    A number is considered perfect if its digits sum up to exactly 10.

    Given a positive integer n, return the n-th perfect number.

    For example, given 1, you should return 19. Given 2, you should return 28.
    :param n: positive integer
    :return:
    """
    if n <= 0 or n >= 10:
        return None

    n_2 = 10 - n

    return int(str(n) + str(n_2))


if __name__ == "__main__":
    print(perfect_digit(4))