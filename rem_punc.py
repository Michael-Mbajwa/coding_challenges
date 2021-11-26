def remove_punctuation(word):
    """A short Python function that takes a strings,representing a sentence,
    and returns a copy of the string with all punctuation removed."""
    new_string = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz '
    for string in word:
        if string.lower() in alphabets:
            new_string += string
    return new_string


print(remove_punctuation('aii.'))