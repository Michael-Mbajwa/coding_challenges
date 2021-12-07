class RunLength:
    """
        Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated
        successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded
        as "4A3B2C1D2A".

        Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists
        solely of alphabetic characters. You can assume the string to be decoded is valid.
        :return:
        """
    def __init__(self):
        self.encoded_string = ""
        self.decoded_string = ""

    def encode(self, string):
        self.encoded_string = ""
        focus = string[0]
        i = 0
        while i < len(string):
            count = 1
            while (i + 1) < len(string) and focus == string[i + 1]:
                count += 1
                i += 1
            self.encoded_string += str(count)
            self.encoded_string += focus

            if (i + 1) < len(string):
                i += 1
                focus = string[i]
            else:
                i += 1
        return self.encoded_string

    def decode(self, string):
        self.decoded_string = ""
        numbers = string[::2]
        letters = string[1::2]
        for i in range(len(letters)):
            self.decoded_string += letters[i] * int(numbers[i])

        return self.decoded_string


if __name__ == "__main__":
    c = RunLength()
    print(c.decode("4A3B2C1D2A"))
    print(c.decode("1A5B6I1T9O"))

    print(c.encode("ABBBBBIIIIIITOOOOOOOOO"))
    print(c.encode("AAAABBBCCDAA"))