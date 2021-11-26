def letters_count():
    """A Python program that inputs a list of words,
    and outputs how many times each alphabet appears in the list."""
    x = input('Provide a word and lets count how many times each alphabet appears: ')
    strings = []
    for alpha in x:
        if alpha != ' ':
            strings.append(alpha.lower())

    count_letters = {}
    length_strings = len(strings)
    for i in range(length_strings):
        count = 1
        for j in range(length_strings):
            if i != j:
                if strings[i] == strings[j]:
                    count += 1

        if strings[i] not in count_letters:
            count_letters[strings[i]] = count

    for key, value in count_letters.items():
        print('Alphabet {0} appears {1} times.'.format(key, value))


letters_count()