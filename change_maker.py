def make_change():
    """A Python program that can “make change.” The program can take two numbers as input,
    one that is a monetary amount charged and the other that is a monetary amount given. It should
    then return the number of each kind of bill and coin to give back as change for the difference
    between the amount given and the amount charged. The values assigned to the bills and coins are
    be based on the monetary system of Nigeria.
    Try to design your program so that it returns as few bills and coins as possible."""
    amount_charged = eval(input('Input monetary amount charged in Nigerian Naira: '))
    amount_given = eval(input('Input monetary amount given in Nigerian Naira: '))
    change = amount_given - amount_charged
    currencies = [1000, 500, 200, 100, 50, 20, 10, 5]
    changes = []
    if change < 0:  # Considers when a customer under pays.
        print('The customer owes {0} Naira.'.format((-1 * change)))
    elif change == 0:
        print('The customer has no change.')
    elif change < 5:  # Considers when the change is below the smallest unit of Naira notes.
        print('Your {0} Naira change will be provided as coins.'.format(change))
    else:
        for currency in currencies:
            if change - currency >= 0:
                while change >= currency:  # This code makes sure that the next available currency isn't considered
                    # until the current currency cannot subtract the available change.
                    changes.append(currency)
                    change = change - currency

        count_numbers = {}  # This code counts each currency and its number of occurrences.
        length_changes = len(changes)
        for i in range(length_changes):
            count = 1
            for j in range(length_changes):
                if i != j:  # Ensures you don't compare a number to itself to avoid duplicated counts.
                    if changes[i] == changes[j]:
                        count += 1

            if changes[i] not in count_numbers:  # Ensures that a value in the dictionary is not repeatedly stored.
                count_numbers[changes[i]] = count

        print('Give the customer the following change: ')
        for key, value in count_numbers.items():
            print('{0} - {1} Naira note(s).'.format(value, key))
        print('And {0} Naira coins.'.format(change))