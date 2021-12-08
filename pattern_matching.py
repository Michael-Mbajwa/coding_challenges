# Using a brute-force algorithm
def pattern_matching(T, P):
    """Given two strings T and P, where T is a text string and P, a pattern string.
    Return the lowest index of T at which substring P begins( or else -1)
    :param T: text string of length n
    :param P: pattern string of length m
    """
    n = len(T)
    m = len(P)

    for i in range(n - m + 1):
        k = 0
        while k < m and P[k] == T[i+k]:
            k += 1
        if k == m:
            return i
    return -1


if __name__ == "__main__":
    test = pattern_matching("zeeman", "man")
    print(test)

    test2 = pattern_matching(T="abacaabaccabacabaabb", P="abacab")
    print(test2)