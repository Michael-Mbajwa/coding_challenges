def each_palindrome(string):
    """
    This problem was asked by Google.

    Given a string, split it into as few strings as possible such that each string is a palindrome.

    For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

    Given the input string abc, return ["a", "b", "c"].
    :param string:
    :return:
    """
    string_copy = string
    result = []
    while string_copy:
        length = len(string_copy)
        for i in range(length):
            current = string_copy[:i+1]
            if current == current[::-1]:
                if result:
                    for word in result:
                        if word in current:
                            result.remove(word)

                result.append(current)
        x = len(result[-1])
        string_copy = string_copy[x:]

    return result


if __name__ == "__main__":
    print(each_palindrome("racecarannakayak"))