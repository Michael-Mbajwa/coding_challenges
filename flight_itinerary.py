def special_iterator(x, flights, start):
    walk = None
    index = None
    for i in range(x):
        if flights[i][0] == start:
            if walk and walk > flights[i]:
                walk = flights[i]
                index = i
            elif not walk:
                walk = flights[i]
                index = i
    return walk, index


def flight_itinerary(flights, start):
    """
    This problem was asked by Facebook.

    Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a
    starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple
    possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

    For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
    starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

    Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

    Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should
    return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
    However, the first one is lexicographically smaller.
    """
    x = len(flights)
    itinerary = [None] * (x+1)
    itinerary[0] = start
    walk, index = special_iterator(x, flights, start)

    itinerary[1] = walk[1]
    flights.pop(index)
    n = 2
    while n < (x+1):
        temp, index = special_iterator(len(flights), flights, itinerary[n-1])

        if temp is None:
            return None

        itinerary[n] = temp[1]
        flights.pop(index)
        n += 1

    return itinerary


if __name__ == "__main__":
    print(flight_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))














# Initial code I had written
def initial(flights, start):
    x = len(flights)
    itinerary = [None] * (x + 1)
    itinerary[0] = start
    walk = None
    index = None
    for i in range(x):
        if flights[i][0] == start:
            if walk and walk > flights[i]:
                walk = flights[i]
                index = i
            elif not walk:
                walk = flights[i]
                index = i

    itinerary[1] = walk[1]
    flights.pop(index)
    n = 2
    while n < (x + 1):
        temp = None
        for i in range(len(flights)):
            if flights[i][0] == itinerary[n - 1]:
                if temp and temp > flights[i]:
                    temp = flights[i]
                    index = i
                elif not temp:
                    temp = flights[i]
                    index = i

        if temp is None:
            return None

        itinerary[n] = temp[1]
        flights.pop(index)
        n += 1

    return itinerary