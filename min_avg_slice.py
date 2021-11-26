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


def min_avg_two_slice(arr):
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
