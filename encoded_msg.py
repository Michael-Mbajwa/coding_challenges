def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def encoded_msg(msg):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

    You can assume that the messages are decode-able. For example, '001' is not allowed.
    """
    mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}
    messages = set()
    multiple = 10**(len(str(msg))-1)
    while multiple >= 10:
        quo = msg // multiple
        rem = msg % multiple
        if quo <= 26 and rem <= 26:
            messages.add(get_key(quo, mapping) + get_key(rem, mapping))
            messages.add(get_key(rem, mapping) + get_key(quo, mapping))
        multiple = multiple / 10

    return len(messages) + 1


print(encoded_msg(111))