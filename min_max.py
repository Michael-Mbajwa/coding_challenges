def minmax(data):
    """A naive function that takes a sequence of one or more numbers, and returns the smallest and largest numbers,
    in the form of a tuple of length two."""
    length_data = len(data)
    if len(data) == 0:
        return 'This is an empty sequence.'
    elif length_data == 1:
        return "This sequence contains only one item."
    else:
        smallest = data[0]
        for x in range(len(data)):
            value = data[x]
            for y in data:
                if y < value:
                    if y < smallest:
                        smallest = y
                    else:
                        smallest
                else:
                    if value < smallest:
                        smallest = value
                    else:
                        smallest

        largest = data[0]
        for a in range(len(data)):
            value = data[a]
            for b in data:
                if b > value:
                    if b > largest:
                        largest = b
                    else:
                        largest
                else:
                    if value > largest:
                        largest = value
                    else:
                        largest

        result = [smallest, largest]
        return tuple(result)


print(minmax([4, 5, 7, 3, 6]))