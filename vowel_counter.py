def vowel_counter(strings):
    """A short Python function that counts the number of vowels in a given
    character string."""
    strings = strings.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = 0
    for string in strings:
        if string in vowels:
            count_vowels += 1

    return count_vowels


print(vowel_counter('michael'))