import random
import numpy as np


def is_multiple(a, b):
    """A function that calculates multiples"""

    yes = 'Yes! {0} is a multiple of {1}.'.format(a, b)
    No = 'No! {0} is not a multiple of {1}.'.format(a, b)
    if a % b == 0:
        return print(yes)
    else:
        return print(No)


# Greatest Common divisor function
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n


def minmax(data):
    """A function that takes a sequence of one or more numbers, and returns the smallest and largest numbers,
    in the form of a tuple of length two."""
    length_data = len(data)
    if len(data) == 0:
        return print('This is an empty sequence.')
    elif length_data == 1:
        return print("This sequence contains only {0}.".format(data[0]))
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
        return print('A tuple with the smallest and largest values in the sequence:'
                     '{0}'.format(tuple(result)))


# R-1.4
def sumsqr():
    """ A short Python function that takes a positive integer n and
    returns the sum of the squares of all the positive integers smaller than n."""
    n = eval(input('Please input a positive integer: '))
    y = str(n)

    if n <= 0:
        print('Sorry, I cannot work with this value.')
    else:
        values = []
        while n > 0:
            n -= 1
            values.append(n)
        print('Values less than {0} are {1}'.format(y, values))
        sum_of_squares = sum((value ** 2) for value in values)
        return print('The sum of squares of all positive integers smaller than {0} is {1}'.
                     format(y, sum_of_squares))


# R-1.6
def sumsqrodd():
    """A short Python function that takes a positive integer n and
    returns the sum of the squares of all the odd positive integers smaller than n."""
    n = eval(input('Please input a positive integer: '))
    y = str(n)

    if n <= 0:
        print('Sorry, I cannot work with this value.')
    else:
        values = []
        n -= 1
        while n > 0:
            if n % 2 != 0:
                values.append(n)
            n -= 1
        print('Odd values less than {0} are {1}'.format(y, values))
        sum_of_squares = sum((value ** 2) for value in values)
        return print('The sum of squares of all positive integers smaller than {0} is {1}'.
                     format(y, sum_of_squares))


# R-1.11
def double_value():
    """Demonstrating how to use Python’s list comprehension syntax to produce
    the list [1, 2, 4, 8, 16, 32, 64, 128, 256]."""
    value = eval(input('Present any integer value: '))
    list_double_value = [1]
    for number in range(1, value):
        value_doubled = list_double_value[-1] * 2
        list_double_value.append(value_doubled)

    return print('The double values of all numbers from 1 to {0} are {1}.'
                 .format(value, list_double_value))


# R-1.12
def my_choice(seq):
    """Using only the randrange function, implement your own version of the choice function."""
    len_seq = len(seq)
    i = random.randrange(len_seq)
    result = seq[i]
    return print(result)


# C-1.13
def reverse_list(s):
    """A function that reverses a list of n integers,
    so that the numbers are listed in the opposite order than they were before"""
    n = len(s)
    reversed_list = []
    for i in range(-1, -(n + 1), -1):
        item = s[i]
        reversed_list.append(item)
    return print(reversed_list)


# C-1.14
def distinct_pair(s):
    """A short Python function that takes a sequence of integer values and
    determines if there is a distinct pair of numbers in the sequence whose product is odd."""
    pairs_with_odd_products = []
    len_pairs = len(pairs_with_odd_products)
    n = len(s)
    for a in range(n):
        initial_value = s[a]
        for b in range(n):
            if a != b:
                next_value = s[b]
                product = initial_value * next_value
                if product % 2 != 0:
                    tuple_product_pairs = tuple([initial_value, next_value])
                    x, y = tuple_product_pairs
                    if (x, y) not in pairs_with_odd_products and (y, x) not in pairs_with_odd_products:
                        pairs_with_odd_products.append(tuple_product_pairs)

    return print(pairs_with_odd_products)


# C-1.15
def distinct(s):
    """A Python function that takes a sequence of numbers and
    determines if all the numbers are different from each other (that is, they are distinct)."""
    n = len(s)
    condition = True
    for i in range(n):
        value_i = s[i]
        for j in range(n):
            if i != j:
                value_j = s[j]
                if value_i == value_j:
                    condition = False
    if not condition:
        return print('This sequence {0} has duplicates.'.format(s))
    else:
        return print('This sequence {0} has no duplicates.'.format(s))


# C-1.18
def special_list():
    """A function that produces the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]."""
    x = eval(input('Enter an integer that indicates the length of required list: '))
    unique_list = []
    for i in range(1, x + 1):
        value = sum(y for y in range(i))
        list_value = 2 * value
        unique_list.append(list_value)

    return print(unique_list)


# C-1.20
def shuffle_method(sequence):
    """Python’s random module includes a function shuffle(data) that accepts a list of elements
    and randomly reorders the elements so that each possi- ble order occurs with equal probability.
    The random module includes a more basic function randint(a, b) that returns a uniformly
    random integer from a to b (including both endpoints). Using only the randint function,
    implement your own version of the shuffle function."""
    sequence_copy = sequence[:]
    reshuffled_list = []
    length_sequence = len(sequence_copy)

    while sequence_copy:
        if length_sequence == 1:
            value = sequence_copy[0]
            reshuffled_list.append(value)
            del sequence_copy[0]
            length_sequence -= 1

        else:
            rand_int = random.randint(0, (length_sequence - 1))
            new_value = sequence_copy[rand_int]
            reshuffled_list.append(new_value)
            del sequence_copy[rand_int]
            length_sequence -= 1

    return print(reshuffled_list)


# C-1.24
def vowel_counter(strings):
    """A short Python function that counts the number of vowels in a given
    character string."""
    strings = strings.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = 0
    for string in strings:
        if string in vowels:
            count_vowels += 1

    return print(count_vowels)


# C-1.25
def remove_punctuation(word):
    """A short Python function that takes a strings,representing a sentence,
    and returns a copy of the string with all punctuation removed."""
    new_string = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz '
    for string in word:
        if string.lower() in alphabets:
            new_string += string
    return print(new_string)


# Collects a number from the user and forms stars with it. For example if 3 is passed, it will produce:
# *
# **
# ***
# **
# *
def form_stars():
    n = eval(input('Provide a number: '))
    star = '*'
    for i in range(1, n + 1):
        print(star * i)
    for j in range(n - 1, 0, -1):
        print(star * j)


# P-1.30
def two_division():
    """A Python program that can take a positive integer greater than 2 as input and write out the
    number of times one must repeatedly divide this number by 2 before getting a value less than 2"""
    number = eval(input('Please provide an integer grater than 2: '))
    count = 0
    if number > 2:
        remainder = number / 2
        count += 1
        while remainder >= 2:
            remainder = remainder // 2
            count += 1
        print('You can repeatedly divide {0} by 2 {1}times before getting a '
              'value less than 2.'.format(number, count))
    else:
        print('Please obey the rule - Provide a positive integer greater than 2.')


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


def binary_gap(n):
    """
    A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
    both ends in the binary representation of N. For example, number 9 has binary representation 1001 and contains
    a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps:
    one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap
    of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary
    representation 100000 and has no binary gaps.
    Write a function:
    def solution(N) that, given a positive integer N, returns the length of its longest binary gap.
    The function should return 0 if N doesn't contain a binary gap.
    For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and
    so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary
    representation '100000' and thus no binary gaps.
    Write an efficient algorithm for the following assumptions: N is an integer within the range [1..2,147,483,647].
    """
    if n in range(1, 2147483648):
        if n < 0:
            return

        val = format(n, 'b')
        print(val)

        if len(val) <= 2:
            return 0

        gaps = []

        for i in range(1, len(val) - 1):
            if val[i - 1] == '1' and val[i] == '0':
                count = 1
                while (count + i) < (len(val) - 1) and val[count + i] == '0':
                    count += 1
                if count + i < len(val) and val[count + i] == '1':
                    gaps.append(count)
            else:
                gaps.append(0)

        return max(gaps)

    return 'Not within range'


def cyclic_rotation(arr, k):
    """
    An array A consisting of N integers is given. Rotation of the array means that each element is shifted right
    by one index, and the last element of the array is moved to the first place. For example, the rotation of
    array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the
    first place).
    The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
    Write a function:
    def solution(A, K)
    that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
    For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
    the function should return [9, 7, 6, 3, 8]. Three rotations were made:
    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    For another example, given
    A = [0, 0, 0]
    K = 1
    the function should return [0, 0, 0]
    Given
    A = [1, 2, 3, 4]
    K = 4
    the function should return [1, 2, 3, 4]
    Assume that:
        N and K are integers within the range [0..100];
        each element of array A is an integer within the range [−1,000..1,000].
    In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
    """
    for j in range(1, k + 1):
        temp_val = arr[0]
        for i in range(len(arr)):
            if (i + 1) < len(arr):
                temp_val, arr[i + 1] = arr[i + 1], temp_val
            elif (i + 1) == len(arr):
                arr[0] = temp_val
        print('Rotation {0}:'.format(j), arr)

    return arr


def perm_check(arr):
    """
    A non-empty array A consisting of N integers is given.
    A permutation is a sequence containing each element from 1 to N once, and only once.
    For example, array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
        A[3] = 2
    is a permutation, but array A such that:
        A[0] = 4
        A[1] = 1
        A[2] = 3
    is not a permutation, because value 2 is missing.
    The goal is to check whether array A is a permutation.
    """
    max_arr = max(arr)
    perms = [i for i in range(max_arr + 1) if i > 0]
    if sorted(arr) == perms:
        return 1
    else:
        return 0


def missing_integer(arr):
    """
    Write a function: that, given an array A of N integers, returns the smallest positive integer (greater than 0)
    that does not occur in A. For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
    Given A = [1, 2, 3], the function should return 4.
    Given A = [−1, −3], the function should return 1.
    Write an efficient algorithm for the following assumptions:
    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
    """
    min_value = min(arr)
    max_value = max(arr)

    if max_value <= 0:
        return 1

    if max_value > 0:
        for i in range(min_value, max_value + 1):
            if i > 0 and i not in arr:
                return i

    if min_value > 0:
        temp = min_value - 1
        while temp > 0:
            if temp not in arr:
                return temp

    found = False
    while not found:
        temp = max_value + 1
        if temp not in arr:
            return temp
        found = True


def prefix_sums(arr):
    p = [0] * len(arr)
    for i in range(len(arr)):
        if i == 0:
            p[i] = arr[i]
        else:
            p[i] = p[i - 1] + arr[i]
    return p


def count_total(a, x, y):
    p = prefix_sums(a)
    if x == 0:
        return p[y]
    else:
        return p[y] - p[x - 1]


def passing_cars(arr):
    """
    A non-empty array A consisting of N integers is given. The consecutive elements of array A represent
    consecutive cars on a road.
    Array A contains only 0s and/or 1s:
        0 represents a car traveling east,
        1 represents a car traveling west.
    The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when
    P is traveling to the east and Q is traveling to the west.
    For example, consider array A such that:
        A[0] = 0
        A[1] = 1
        A[2] = 0
        A[3] = 1
        A[4] = 1
    We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
    """
    if len(arr) <= 1000000000:
        result = []
        zero_index = [index for index, value in enumerate(arr) if value == 0]
        one_index = [index for index, value in enumerate(arr) if value == 1]

        for p in zero_index:
            for z in one_index:
                if p < z:
                    result.append((p, z))

        return len(result)
    return 'Not within range'


def count_div(a, b, k):
    """
    Write a function:
    def solution(A, B, K)
    that, given three integers A, B and K, returns the number of integers within the range [A..B]
    that are divisible by K, i.e.:
    { i : A ≤ i ≤ B, i mod K = 0 }
    For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers
    divisible by 2 within the range [6..11], namely 6, 8 and 10.
    Write an efficient algorithm for the following assumptions:
        A and B are integers within the range [0..2,000,000,000];
        K is an integer within the range [1..2,000,000,000];
        A ≤ B.
    """
    if a < b and b - a < 2000000001 and k in range(1, 2000000001):
        count = 0
        for i in range(a, b + 1):
            if i % k == 0:
                count += 1

        return count

    return 'Doesn\'t satisfy function constraints.'


def MinAvgTwoSlice(arr):
    """
    Find the minimal average of any slice containing at least two elements.
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a
slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of
A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise,
the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).
For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:
        slice (1, 2), whose average is (2 + 2) / 2 = 2;
        slice (3, 4), whose average is (5 + 1) / 2 = 3;
        slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.
Write a function:
    def solution(A)
that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the
minimal average. If there is more than one slice with a minimal average, you should return the smallest starting
position of such a slice.
For example, given array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.
Write an efficient algorithm for the following assumptions:
        N is an integer within the range [2..100,000];
        each element of array A is an integer within the range [−10,000..10,000].
    """
    slices_avg = {}
    for i in range(len(arr) - 1):
        slices_avg[i] = None
        for j in range(i + 1, len(arr)):
            index_avg = (count_total(arr, i, j)) / ((j - i) + 1)
            if slices_avg[i] is None:
                slices_avg[i] = index_avg
            else:
                if slices_avg[i] > index_avg:
                    slices_avg[i] = index_avg

    return min(slices_avg, key=slices_avg.get)


def add_up(arr, k):
    """
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    """
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return None


def prod_arr(arr):
    """
    Given an array of integers, return a new array such that each element at index i of the new array is the
    product of all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    new_arr = []
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if i != j:
                prod *= arr[j]
        new_arr.append(prod)

    return new_arr


def merge_sorted(arr):
    """
    Return a new sorted merged list from K sorted lists, each with size N.
    For example, if we had [[10, 15, 30], [12, 15, 20], [17, 20, 32]], the result should be
    [10, 12, 15, 15, 17, 20, 20, 30, 32].
    """
    # Naive solution
    merged_list = list()
    for inn_arr in arr:
        for i in inn_arr:
            merged_list.append(i)

    return sorted(merged_list)


print(merge_sorted([[10, 15, 30], [12, 15, 20], [17, 20, 32]]))