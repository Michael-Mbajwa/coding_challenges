import heapq


def orig_sent(words_set, string):
    """
    Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
    If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then
    return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should
    return ['the', 'quick', 'brown', 'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either
    ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
    """
    indexes = []
    for word in words_set:
        if string.find(word) not in indexes:
            indexes.append(string.find(word))
    result = [None] * len(indexes)
    i = 0
    heapq.heapify(indexes)
    while indexes:
        if len(indexes) > 1:
            x, y = heapq.nsmallest(2, indexes)
            result[i] = string[x:y]
            i += 1
            heapq.heappop(indexes)
        else:
            result[i] = string[heapq.heappop(indexes):]

    return result


if __name__ == "__main__":
    print(orig_sent({'quick', 'brown', 'the', 'fox'}, "thequickbrownfox"))
    print(orig_sent({'bed', 'bath', 'bedbath', 'and', 'beyond'}, "bedbathandbeyond"))