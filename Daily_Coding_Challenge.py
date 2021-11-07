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

