from collections import defaultdict


def zigzag(string, k):
    """
    Given a string and a number oflines k, print the string in zigzag form. In zigzag, characters are printed out
    diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.
    For example, given the sentence "thisisazigzag" and k
    t       a       g
     h     s z     a
      i   i   i   z
        s       g
    :param string:
    :param k:
    :return:
    """
    # Initialize dictionary. The number of keys depends on the provided k value
    g = defaultdict(str)
    for j in range(k):
        g[j] = ""

    count = 0
    i = 0

    # This while loop prints the first line of the zig zag
    while count < k:
        g[count] += (" " * count) + string[i]
        count += 1
        i += 1

    while i < len(string):
        if count == 0:  # If count is 0, it means our zigzag is coming down.
            count = 1
            count2 = 1  # This helps in creating the spaces between numbers
            while count < k and i < len(string):
                g[count] += (" " * count2) + string[i]
                count += 1
                count2 += 2  # Looking at the zigzag, you will see spaces between numbers increase by 2 after each line
                i += 1

        elif count == k:  # If count equals to provided k, our zigzag is going up
            count = k - 2
            count2 = 1
            while count >= 0 and i < len(string):
                g[count] += (" " * count2) + string[i]
                count2 += 2
                count -= 1
                i += 1
            count = 0

    for key, value in g.items():
        print(value)


if __name__ == "__main__":
    zigzag("thisisanotherzigzag", 5)