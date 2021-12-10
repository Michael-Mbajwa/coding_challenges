# Super fast alternative way to solve this using maps
def rgb(arr):
    """

    Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs
    come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

    Do this in linear time and in-place.

    For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become
    ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
    :return:
    """
    rgb_dic = {}
    for char in arr:
        if char not in rgb_dic:
            rgb_dic[char] = 1
        else:
            rgb_dic[char] += 1

    result = list(("R" * rgb_dic['R']) + ("G" * rgb_dic['G']) + ("B" * rgb_dic['B']))

    return result


if __name__ == "__main__":
    print(rgb(['G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G',
               'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R', 'G', 'G', 'B', 'R', 'R', 'B', 'R']))