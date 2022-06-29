import random
import numpy as np
import heapq


def xor_linked_list():
    """
    An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
    it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
    it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

    If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
    dereference_pointer functions that converts between nodes and memory addresses.
    """
    return None


def uni_val(tree):
    """
    A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

    Given the root to a binary tree, count the number of unival subtrees.

    For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
    """
    return None


def pi_estimate():
    """
    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

    Hint: The basic equation of a circle is x2 + y2 = r2.
    :return:
    """
    return None


def rand_prob(element):
    """
    Given a stream of elements too large to store in memory, pick a random element from the
    stream with uniform probability.
    :param element:
    :return:
    """
    return None


def last_order():
    """
    You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure
    to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

    You should be as efficient with time and space as possible.
    :return:
    """
    return None


def builder():
    """
    A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing
    cost while ensuring that no two neighboring houses are of the same color.

    Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
    return the minimum cost which achieves this goal.
    :return:
    """
    return None


def intersect_ll():
    """
    Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

    For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

    In this example, assume nodes with the same value are the exact same node objects.

    Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
    :return:
    """
    return None


def board():
    """
    This problem was asked by Google.

    You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
    Each False boolean represents a tile you can walk on.

    Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach
    the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down,
    and right. You cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:

    [[f, f, f, f],
    [t, t, f, t],
    [f, f, f, f],
    [f, f, f, f]]

    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the
    end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
    :return:
    """
    return None


def lock_bin_tree():
    """
    Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants
    or ancestors are not locked.

    Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should
    lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should
    unlock it and return true.

    You may augment the node to add parent pointers or any other property you would like. You may assume the class is
    used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h),
    where h is the height of the tree.
    """
    return None


def reg_ex():
    """
    Implement regular expression matching with the following special characters:

    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element

    That is, implement a function that takes in a string and a valid regular expression and returns whether or not the
    string matches the regular expression.

    For example, given the regular expression "ra." and the string "ray", your function should return true.
    The same regular expression on the string "raymond" should return false.

    Given the regular expression ".*at" and the string "chat", your function should return true.
    The same regular expression on the string "chats" should return false.
    :return:
    """
    return None


def remove_k():
    """
    Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be
    smaller than the length of the list.

    The list is very long, so making more than one pass is prohibitively expensive.

    Do this in constant space and in one pass.
    :return:
    """
    return None


def justify_text():
    """
    This problem was asked by Palantir.

    Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of
    strings which represents each line, fully justified.

    More specifically, you should have as many words as possible in each line. There should be at least one space
    between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be
    distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

    If you can only fit one word on a line, then you should pad the right-hand side with spaces.

    Each word is guaranteed not to be longer than k.

    For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
    and k = 16, you should return the following:

    ["the  quick brown", # 1 extra space on the left
    "fox  jumps  over", # 2 extra spaces distributed evenly
    "the   lazy   dog"] # 4 extra spaces distributed evenly

    :return:
    """
    return None


def trapped_units():
    """
    You are given an array of non-negative integers that represents a two-dimensional elevation map where each element
    is unit-width wall and the integer is the height. Suppose it will rain and all spots between
    two walls get filled up.

    Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

    For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

    Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the
    fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
    :return:
    """
    "https://www.geeksforgeeks.org/trapping-rain-water/"
    return None


def n_n_board():
    """
    This problem was asked by Microsoft.

    You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board
    where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row,
    column, or diagonal.
    :return:
    """
    return None


def out_of_order(arr):
    """
    This problem was asked by Google.

    We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i]
    and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

    Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

    You may assume each element in the array is distinct.

    For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1),
    and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
    :param arr:
    :return:
    """
    return None


def rand():
    """
    Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a
    function rand7() that returns an integer from 1 to 7 (inclusive).
    :return:
    """
    return None


def reconstruct():
    """
    This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

    :return:
    """
    return None


def max_sum(arr):
    """
    This problem was asked by Amazon.

    Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

    For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
    42, 14, -5, and 86.

    Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

    Do this in O(N) time.
    :param arr:
    :return:
    """
    return None


def binary_tree_arithmetic():
    """
    This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
    :return:
    """
    return None


def longest_palindrome():
    """
    This problem was asked by Amazon.

    Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum
    length, return any one.

    For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of
    "bananas" is "anana".
    :return:
    """
    return None


def sub_dir():
    """
    I will solve this problem with a tree data structure

    This problem was asked by Google.
    Suppose we represent our file system by a string in the following manner:
    The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
    dir
        subdir1
        subdir2
            file.ext

    The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.
    The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:
    dir
        subdir1
            file1.ext
            subsubdir1
        subdir2
            subsubdir2
                file2.ext

    The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext
    and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
    containing a file file2.ext.

    We are interested in finding the longest (number of characters) absolute path to a file within our file system. For
    example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its
    length is 32 (not including the double quotes).

    Given a string representing the file system in the above format, return the length of the longest absolute path
    to a file in the abstracted file system. If there is no file in the system, return 0.

    Note:

    The name of a file contains at least a period and an extension.

    The name of a directory or sub-directory will not contain a period.
    :return: None
    """
    return None


def shuffle():
    """

Daily Coding Problem

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input,
write a function that shuffles a deck of cards represented as an array using only swaps.

It should run in O(N) time.

Hint: Make sure each one of the 52! permutations of the deck is equally likely.
    :return:
    """
    return None


def LRU():
    """
    This problem was asked by Google.

    Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain
    the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least recently used item.
    get(key): gets the value at key. If no such key exists, return null.

    Each operation should run in O(1) time.
    :return:
    """
    return None


def queue():
    """
    This problem was asked by Apple.

    Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the
    following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
    :return:
    """
    return None


def sudoku_solver():
    """
    This problem was asked by Dropbox.

    Sudoku is a puzzle where you're given a partially-filled 9 by 9 grid with digits. The objective is to fill the
    grid with the constraint that every row, column, and box (3 by 3 subgrid) must contain all of the digits
    from 1 to 9.

    Implement an efficient sudoku solver.
    :return:
    """
    return None


def url_shortener():
    """
    Implement a URL shortener with the following methods:

    shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
    restore(short), which expands the shortened string into the original url. If no such shortened string exists,
    return null.

    Hint: What if we enter the same URL twice?
    :return:
    """
    return None


def color_graph():
    """
    This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether
each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
    :return:
    """
    return None


def break_string():
    """
    This problem was asked by Amazon.

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or
less. You must break it up so that words don't break across lines. Each line has to have the maximum possible
amount of words. If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should
return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.
    :return:
    """
    return None


def find_index():
    """
    This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't
exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
    :return:
    """
    return None


def multiset():
    """
    This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that
add up to the same sum.
    :return:
    """
    return None


def house_robber():
    """
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
    stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems
    connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
    of money you can rob tonight without alerting the police.

    Test Case 1:
    Input: [50, 60, 1, 10]
    Output: 70

    Test Case 2:
    Input: [100, 200, 50, 40, 120]
    Output: 320

    :return:
    """
    return None


def integer_exponentiation():
    """
     This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
    :return:
    """
    return None


def zeros_matrix(matrix):
    """
    This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting
at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

    Right, then down
    Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
    :param matrix:
    :return:
    """
    return None


def target_word():
    """
    This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in
the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word
'MASS', you should return true, since it's the last row.
    :return:
    """
    return None


def special_arrangement():
    """
    Problem Description

Given a array A of non negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Problem Constraints

1 <= len(A) <= 100000
0 <= A[i] <= 2*109

Input Format

First argument is an array of integers.

Output Format

Return a string representing the largest number.

Example Input

Input 1:

     A = [3, 30, 34, 5, 9]

Input 2:

     A = [2, 3, 9, 0]

Example Output

Output 1:

     "9534330"

Output 2:

     "9320"

Example Explanation

Explanation 1:

     A = [3, 30, 34, 5, 9]
     Reorder the numbers to [9, 5, 34, 3, 30] to form the largest number.

Explanation 2:

     Reorder the numbers to [9, 3, 2, 0] to form the largest number 9320.
    :return:
    """
    return None


def auto_complete():
    """
    You have an array of words and a string, and you need to find all possible words that start with the given string.
    Test Case 1:

    Input: 	words = [“yash”, “neha”, “swati”, “lakhan”, “yasin”], str = “ya”
    Output: [“yash”, “yasin”]

Test Case 2:

    Input: 	words = [“court”, “cat”, “catchy”, “cipher”, “can”], str = “cat”
    Output: [“cat”, “catchy”]
    :return:
    """
    return None


def equilibrium_index():
    """
    You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of
elements at higher indexes.

NOTE:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.

Problem Constraints

    1<=N<=1e5
    -1e5<=A[i]<=1e5

Input Format

First arugment contains an array A .

Output Format

Return the equilibrium index of the given array. If no such index is found then return -1.

Example Input

Input 1:

    A=[-7, 1, 5, 2, -4, 3, 0]

Input 2:

    A=[1,2,3]

Example Output

Output 1:

    3

Output 2:

    -1

Example Explanation

Explanation 1:

    3 is an equilibrium index, because:
    A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Explanation 1:

    There is no such index.
    :return:
    """
    return None


def knight_tour():
    """
    This problem was asked by Google.

    A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

    Given N, write a function to return the number of knight's tours on an N by N chessboard.
    :return:
    """
    return None


def clockwise_spiral(matrix):
    """
    This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12

    :param matrix:
    :return:
    """
    return None


def unbiased_coin():
    """
    Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not
    50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

    Write a function to simulate an unbiased coin toss.
    :return:
    """
    return None


def LFU():
    """
    This problem was asked by Google.

    Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and
    contain the following methods:

    set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
    then it should also remove the least frequently used item. If there is a tie, then the least recently used key
    should be removed.
    get(key): gets the value at key. If no such key exists, return null.

    Each operation should run in O(1) time.
    :return:
    """
    return None


def special_chessboard():
    """
    This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops
that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the
number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the
same as (2, 1).

For example, given M = 5 and the list of bishops:

    (0, 0)
    (1, 2)
    (2, 2)
    (4, 0)

The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]

You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
    :return:
    """
    return None


def largest_product():
    """
    This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
    :return:
    """
    return None


def kth_largest_element(arr, k):
    """
    You have been given an array of numbers and an integer k. You need to find the kth largest number in that array in
    O(n) complexity
    :param arr:
    :param k:
    :return:
    """
    return None


def rand5():
    """
    This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function
rand5() that returns an integer from 1 to 5 (inclusive).
    :return:
    """
    return None


def largest_value_path():
    """
    This problem was asked by Google.

In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most
frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the
path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is
infinite, then return null.

The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th
node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges
are possible, as well as multi-edges.

For example, the following input graph:

ABACA

[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]

Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

The following input graph:

A

[(0, 0)]

Should return null, since we have an infinite loop.
    :return:
    """
    return None


def reverse_linked_list():
    """
    This problem was asked by Google.

    Given the head of a singly linked list, reverse it in-place.
    :return:
    """
    return None


def multiplication_table():
    """
    This problem was asked by Apple.

Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and
j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

Given integers N and X, write a function that returns the number of times X appears as a value in an N by N
multiplication table.

For example, given N = 6 and X = 12, you should return 4, since the multiplication table looks like this:

| 1 | 2 | 3 | 4 | 5 | 6 |

| 2 | 4 | 6 | 8 | 10 | 12 |

| 3 | 6 | 9 | 12 | 15 | 18 |

| 4 | 8 | 12 | 16 | 20 | 24 |

| 5 | 10 | 15 | 20 | 25 | 30 |

| 6 | 12 | 18 | 24 | 30 | 36 |

And there are 4 12's in the table.
    :return:
    """
    return None


def longest_increasing_subsequence():
    """
    This problem was asked by Microsoft.

    Given an array of numbers, find the length of the longest increasing subsequence in the array.
    The subsequence does not necessarily have to be contiguous.

    For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
    subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
    :return:
    """
    return None


def minimum_columns():
    """
    This problem was asked by Google.

You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to
ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is
lexicographically later as you go down each row. It does not matter whether each row itself is ordered
lexicographically.

For example, given the following table:

cba
daf
ghi

This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi

So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef

Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr

Your function should return 3, since we would need to remove all the columns to order it.
    :return:
    """
    return None


def overlapping_intervals(intervals):
    """
    This problem was asked by Snapchat.

    Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals
    have been merged.

    The input list is not necessarily ordered in any way.

    For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
    :return:
    """
    return None


def merged_linked_lists():
    """
    This problem was asked by Google.

    Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
    :return:
    """
    return None


def word_break():
    """
    Given an input string and a dictionary of words, find out if the input string can be segmented into a
    space-separated sequence of dictionary words.

    Dictionary: { i, like, sam, sung, samsung, mobile, ice, cream, icecream, man, go, mango}
    Test Case 1:

    Input: ilike
    Output: Yes

Explanation:

    The string can be segmented as "i like".

Test Case 2:

    Input: ilikesamsung
    Output: Yes

Explanation:

    The string can be segmented as "i like samsung" or "i like sam sung".
    :return:
    """
    return None


def bottom_view():
    """
    Given a Binary Tree, we need to print the bottom view from left to right. A node x is there in output if x is the
    bottommost node at its horizontal distance. The horizontal distance of the left child of a node x is equal
    to the horizontal distance of x minus 1, and that of the right child is the horizontal distance of x plus 1.
    Test Case 1:

    Input:
               1
              / \
             2   8
            / \
           3   7
          / \
         4   6
        /
       5

    Output: [5, 6, 7, 8]

Test Case 2:

    Input:
             20
           /    \
          8      22
         / \    /  \
        5   3  4    25
           / \
         10   14

    Output: [5, 10, 4, 14, 25]
    :return:
    """
    return None


def non_decreasing():
    """
    This problem was asked by Facebook.

    Given an array of integers, write a function to determine whether the array could become non-decreasing by
    modifying at most 1 element.

    For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the
    array non-decreasing.

    Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing
    array.
    :return:
    """
    return None


def deepest_node(bin_tree):
    """
    This problem was asked by Google.

    Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d

    :param bin_tree:
    :return:
    """
    return None


def possible_letters():
    """
    This problem was asked by Yelp.

    Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the
    number could represent. You can assume each valid number in the mapping is a single digit.

    For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return
    [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
    :return:

    https://dev.to/seanpgallivan/solution-letter-combinations-of-a-phone-number-1n91
    """
    return None


def read_7():
    """
    This problem was asked Microsoft.

    Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

    For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “
    :return:
    """
    return None


def invert_binary_tree():
    """
    This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f

should become:

  a
 / \
 c  b
 \  / \
  f e  d

    :return:
    """
    return None


def islands_matrix():
    """
    This problem was asked by Amazon.

    Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents
    water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

    For example, this matrix has 4 islands.

    1 0 0 0 0
    0 0 1 1 0
    0 1 1 0 0
    0 0 0 0 0
    1 1 0 0 1
    1 1 0 0 1
    :return:
    """
    return None


def valid_parenthesis():
    """
    This problem was asked by Google.

    Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make
    the string valid (i.e. each open parenthesis is eventually closed).

    For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we
    must remove all of them.
    :return:
    """
    return None


def valid_binary_search_tree(root):
    """
    This problem was asked by LinkedIn.

    Determine whether a tree is a valid binary search tree.

    A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the
    left child must be less than or equal to the root and the key in the right child must be greater than or equal to
    the root.
    :param root:
    :return:
    """
    return None


def rand_generator():
    """
    This question was asked by Google.

    Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1
    that isn't in l (uniform).
    :return:
    """
    return None


def sorted_courses():
    """
    This problem was asked by Airbnb.

    We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the
    prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.

    Return null if there is no such ordering.

    For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return
    ['CSC100', 'CSC200', 'CSCS300'].
    :return:
    """
    return None


def largest_subtree(root):
    """
    This problem was asked by Apple.

    Given a tree, find the largest tree/subtree that is a BST.

    Given a tree, return the size of the largest tree/subtree that is a BST.
    :param root:
    :return:
    """
    return None


def max_path_sum(root):
    """
    This problem was asked by Google.

    Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one
    node, and does not need to go through the root.
    :return:
    """
    return None


def next_greater_perm():
    """
    This problem was asked by Palantir.

    Given a number represented by a list of digits, find the next greater permutation of a number, in terms of
    lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest
    value/ordering.

    For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1]
    should return [1,2,3].

    Can you perform the operation without allocating extra memory (disregarding the input memory)?
    :return:
    """
    return None


def all_permutations():
    """
    This problem was asked by Microsoft.

    Given a number in the form of a list of digits, return all possible permutations.

    For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
    :return:
    """
    return None


def map_implementation():
    """
    This problem was asked by Stripe.

Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

It should contain the following methods:

    set(key, value, time): sets key to value for t = time.
    get(key, time): gets the key at t = time.

The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

Consider the following examples:

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 2) # set key 1 to value 2 at time 2
d.get(1, 1) # get key 1 at time 1 should be 1
d.get(1, 3) # get key 1 at time 3 should be 2

d.set(1, 1, 5) # set key 1 to value 1 at time 5
d.get(1, 0) # get key 1 at time 0 should be null
d.get(1, 10) # get key 1 at time 10 should be 1

d.set(1, 1, 0) # set key 1 to value 1 at time 0
d.set(1, 2, 0) # set key 1 to value 2 at time 0
d.get(1, 0) # get key 1 at time 0 should be 2
    :return:
    """
    return None


def chess_2d():
    """
    This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
    :return:
    """
    return None


def longest_length():
    """

Daily Coding Problem

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.

    :return:
    """
    return None


def infinite_2d_grid():
    """
    This problem was asked by Google.

    You are in an infinite 2D grid where you can move in any of the 8 directions:

    (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

    You are given a sequence of points and the order in which you need to cover the points.
    Give the minimum number of steps in which you can achieve it. You start from the first point.

    Example:

    Input: [(0, 0), (1, 1), (1, 2)]
    Output: 2

    It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

    :return:
    """
    return None


def two_prime():
    """
    This problem was asked by Alibaba.

    Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

    A solution will always exist. See Goldbach’s conjecture.

    Example:

    Input: 4
    Output: 2 + 2 = 4

    If there are more than one solution possible, return the lexicographically smaller solution.

    If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

    [a, b] < [c, d]

    If a < c OR a==c AND b < d.
    :return:
    """
    return None


def contiguous_sum(arr, k):
    """
    This problem was asked by Lyft.

    Given a list of integers and a number K, return which contiguous elements of the list sum to K.

    For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
    :return:
    """
    return None


def sum_all_primes(n):
    """
    You're given a number n. Write a method sumOfAllPrimes that finds all prime numbers smaller than or equal to n,
    and returns a sum of them.
    For example, we're given the number 15. All prime numbers smaller than 15 are:

    2, 3, 5, 7, 11, 13

    They sum up to 41, so sumOfAllPrimes(15) would return 41.
    :param n: An integer
    :return:
    """
    if not isinstance(n, int):
        return "Not an integer."
    if n <= 1:
        return 1

    return None


def path_leaves_to_root(root):
    """
    This problem was asked by Facebook.

    Given a binary tree, return all paths from the root to leaves.

    For example, given the tree:

   1
  / \
 2   3
    / \
   4   5

    Return [[1, 2], [1, 3, 4], [1, 3, 5]].
    :param root:
    :return:
    """
    return None


def starting_indices():
    """
    This problem was asked by Google.

    Given a word W and a string S, find all starting indices in S which are anagrams of W.

    For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
    :return:
    """
    return None


def lowest_common_ancestor(root):
    """
    This problem was asked by Twitter.

    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    Assume that each node in the tree also has a pointer to its parent.

    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v
    and w as the lowest node in T that has both v and w as descendants
    (where we allow a node to be a descendant of itself).”
    :param root:
    :return:
    """
    return None


def shortest_substring(string, char):
    """
    This problem was asked by Square.

    Given a string and a set of characters, return the shortest substring containing all the characters in the set.

    For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

    If there is no substring containing all the characters in the set, return null.
    :return:
    """
    return None


def reverse_words():
    """
    This problem was asked by Google.

    Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
    return "here world hello"

    Follow-up: given a mutable string representation, can you perform this operation in-place?
    :return:
    """
    return None


def reverse_string_delimiter():
    """
    Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of
    the delimiters. For example, given "hello/world:here", return "here/world:hello"

    Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"
    :return:
    """
    return None


def equivalent_tree(s, t):
    """
    This problem was asked by Google.
    Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
    a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
    The tree s could also be considered as a subtree of itself.
    :param s: non-empty binary tree
    :param t: non-empty binary tree
    :return: True or False
    """
    return None


def second_largest(root):
    """
    This problem was asked by Dropbox.

    Given the root to a binary search tree, find the second largest node in the tree.
    :param root:
    :return:
    """
    return None


def minimum_sum_level(root):
    """
    This problem was asked by Facebook.

    Given a binary tree, return the level of the tree with minimum sum.
    :param root:
    :return:
    """
    return None


def sorted_squares(arr):
    """
    This problem was asked by Google.

    Given a sorted list of integers, square the elements and give the output in sorted order.

    For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
    :param arr: sorted list of integers
    :return:
    """
    return None


def cover_intervals():
    """
    This problem was asked by Google.

    Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
    If there are multiple smallest sets, return any of them.

    For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these
    intervals is {3, 6}.
    :return:
    """
    return None


def del_to_palindrome():
    """
    Given a string which we can delete at most k, return whether you can make a palindrome.

    For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
    :return:
    """
    return None


def max_coins():
    """
    This question was asked by Zillow.

    You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at
    matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom
    right corner.

    For example, in this matrix

    0 3 1 1
    2 0 0 4
    1 5 3 1

    The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
    :return:
    """
    return None


def is_number(string):
    """
    Given a string, return whether it represents a number. Here are the different kinds of numbers:

    "10", a positive integer
    "-10", a negative integer
    "10.1", a positive real number
    "-10.1", a negative real number
    "1e5", a number in scientific notation

    And here are examples of non-numbers:

    "a"
    "x 1"
    "a -2"
    "-"

    :param string:
    :return:
    """
    return None


def sum_two_nodes(root):
    """
    This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15

Return the nodes 5 and 15
    :return:
    """
    return None


def rotate_k():
    """
    This problem was asked by Facebook.

    Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes
    [3, 4, 5, 6, 1, 2]. Try solving this without creating a copy of the list. How many swap or move operations
    do you need.
    :return:
    """
    return None


def square_root(n):
    """
    Given a real number n, find the square root of n. For example, given n = 9, return 3
    :param n: a real number.
    :return:
    """
    return None


def max_profit():
    """
    This problem was asked by Facebook.

    Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
    return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it,
    and you must sell the stock before you can buy it again.

    For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
    :return:
    """
    return None


def deep_clone_ll(head):
    """
    Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the
    linked list, deep clone the list.
    :param head: head of a linked list
    :return:
    """
    return None


def hit_counter():
    """
    This question was asked by Riot Games.

    Design and implement a HitCounter class that keeps track of requests (or hits). It should support the
    following operations:

    record(timestamp): records a hit that happened at timestamp
    total(): returns the total number of hits recorded
    range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

    Follow-up: What if our system has limited memory?
    :return:
    """
    return None


def inorder_successor(root):
    """
    This problem was asked by Amazon.

    Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

    For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35

    You can assume each node has a parent pointer.
    :param root:
    :return:
    """
    return None


def sparse_array():
    """
    This problem was asked by Facebook.

    You have a large array with most of the elements as zero.

    Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

    :return:
    """
    return None


def min_path():
    """
    Given a binary tree, find a minimum path sum from root to a leaf.

    For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1

    :return:
    """
    return None


def largest_rectangle(matrix):
    """
    This question was asked by Google.

    Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing only 1's and return
    its area.

    For example, given the following matrix:

    [[1, 0, 0, 0],
    [1, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 0]]

    Return 4.
    :param matrix:
    :return:
    """
    return None


def minimum_coins():
    """
    This problem was asked by Google.

    Find the minimum number of coins required to make n cents.

    You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

    For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
    :return:
    """
    return None


class PeekableInterface(object):
    """
    This problem was asked by Google.

    Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also
    implements peek(). peek shows the next element that would be returned on next().

    Here is the interface:

    class PeekableInterface(object):
        def __init__(self, iterator):
        pass

        def peek(self):
        pass

        def next(self):
        pass

        def hasNext(self):
        pass
    """


def stacks():
    """
    This problem was asked by Microsoft.

Implement 3 stacks using a single list:

class Stack:
    def __init__(self):
        self.list = []

    def pop(self, stack_number):
        pass

    def push(self, item, stack_number):
        pass

    :return:
    """
    return None


def pivot_partition():
    """
    This problem was asked by Amazon.

    Given a pivot x, and a list lst, partition the list into three parts.

    The first part contains all elements in lst that are less than x
    The second part contains all elements in lst that are equal to x
    The third part contains all elements in lst that are larger than x

    Ordering within a part can be arbitrary.

    For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14].

    :return:
    """
    return None


def nearest_largest():
    """
    This problem was asked by Google.

    Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i,
    where distance is measured in array indices.

    For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

    If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a
    nearest larger integer, then return null.

    Follow-up: If you can preprocess the array, can you do this in constant time?
    :return:
    """
    return None


def swap_two_nodes(root):
    """
    This problem was asked by Google.

    Given the head of a singly linked list, swap every two nodes and return its head.

    For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
    :param root: head of a singly linked list.
    :return:
    """
    return None


def prune_tree():
    """
    Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

    For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0

    should be pruned to:

   0
  / \
 1   0
    /
   1

    We do not remove the tree at the root or its left child because it still has a 1 as a descendant.

    :return:
    """
    return None


def reverse_sort(lst, i, j):
    """
    Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
    :param lst: a list
    :param i: integer
    :param j: integer
    :return:
    """
    return None


def nearest_point():
    """
    This problem was asked by LinkedIn.

    Given a list of points, a central point, and an integer k, find the nearest k points from the central point.

    For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central point (1, 2), and k = 2,
    return [(0, 0), (3, 1)].
    :return:
    """
    return None


def replace_color():
    """
    Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, replace the color of
    the given pixel and all adjacent same colored pixels with C.

    For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

    B B W
    W W W
    W W W
    B B B

    Becomes

    B B G
    G G G
    G G G
    B B B
    :return:
    """
    return None


def generate_number():
    """
    This problem was asked by Triplebyte.

    You are given n numbers as well as n probabilities that sum up to 1. Write a function to generate one of the numbers
    with its corresponding probability.

    For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2], your function should return 1
    10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

    You can generate random numbers between 0 and 1 uniformly.
    :return:
    """
    return None


def shortest_word_distance(word):
    """
    Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words
    in a string.

    For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world",
    return 1 because there's only one word "cat" in between the two words.
    :param word:
    :return:
    """
    return None


def majority_element():
    """
    This problem was asked by MongoDB.

    Given a list of elements, find the majority element, which appears more than half the time
    (> floor(len(lst) / 2.0)).

    You can assume that such element exists.

    For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
    :return:
    """
    return None


def smallest_squared_integers():
    """
    This problem was asked by Facebook.

    Given a positive integer n, find the smallest number of squared integers which sum to n.

    For example, given n = 13, return 2 since 13 = 32 + 22 = 9 + 4.

    Given n = 27, return 3 since 27 = 32 + 32 + 32 = 9 + 9 + 9.
    :return:
    """
    return None


def bottom_right():
    """
    This problem was asked by Slack.

    You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to
    reach the bottom right corner?

    You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

    For example, given the following matrix:

    [[0, 0, 1],
    [0, 0, 1],
    [1, 0, 0]]

    Return two, as there are only two ways to get to the bottom right:

        Right, down, down, right
        Down, right, down, right

    The top left corner and bottom right corner will always be 0.
    :return:
    """
    return None


def shortest_unique_prefix():
    """
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Square.

    Given a list of words, return the shortest unique prefix of each word. For example, given the list:

        dog
        cat
        apple
        apricot
        fish

    Return the list:

        d
        c
        app
        apr
        f
    :return:
    """
    return None


def reverse_polish_notation():
    """
    This problem was asked by Jane Street.

    Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

    The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

    For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent
    to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

    You can assume the given expression is always valid.
    :return:
    """
    return None


def pigeon_hole_duplicate():
    """
    This problem was asked by Google.

    You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. By the pigeonhole principle,
    there must be a duplicate. Find it in linear time and space.
    :return:
    """
    return None


def iterator_class_2d():
    """
    This problem was asked by Uber.

    Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement
    the following methods:

        next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
        has_next(): returns whether or not the iterator still has elements left.

    For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

    Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
    :return:
    """
    return None


def unique_indices():
    """
     This problem was asked by Airbnb.

    Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a
    palindrome.

    For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
    :return:
    """
    return None


def rotate_matrix():
    """
    This problem was asked by Facebook.

    Given an N by N matrix, rotate it by 90 degrees clockwise.

    For example, given the following matrix:

    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

    you should return:

    [[7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]]

    Follow-up: What if you couldn't use any extra space?
    :return:
    """
    return None


def sort_linked_list():
    """
    This problem was asked by Google.

    Given a linked list, sort it in O(n log n) time and constant space.

    For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
    :return:
    """
    return None


def shortest_transformation_sequence():
    """
    This problem was asked by Facebook.

    Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from
    start to end such that only one letter is changed at each step of the sequence, and each transformed word exists
    in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same
    length as start and end and is lowercase.

    For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return
    ["dog", "dot", "dat", "cat"].

    Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no
    possible transformation from dog to cat.
    :return:
    """
    return None


def busiest_period():
    """
    This problem was asked by Amazon.

    You are given a list of data entries that represent entries and exits of groups of people into a building.
    An entry looks like this: {"timestamp": 1526579928, count: 3, "type": "enter"}

    This means 3 people entered the building. An exit looks like this:
    {"timestamp": 1526580382, count: 2, "type": "exit"}

    This means that 2 people exited the building. timestamp is in Unix time.

    Find the busiest period in the building, that is, the time with the most people in the building.
    Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty,
    i.e. with 0 people inside.
    :return:
    """
    return None


def index_start_substring():
    """
    This problem was asked by Dropbox.

    Given a string s and a list of words words, where each word is the same length, find all starting indices of
    substrings in s that is a concatenation of every word in words exactly once.

    For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], since "dogcat" starts
    at index 0 and "catdog" starts at index 13.

    Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings composed of
    "dog" and "cat" in s.

    The order of the indices does not matter.
    :return:
    """
    return None


def flatten_nested_dictionary():
    """
    This problem was asked by Stripe.

    Write a function to flatten a nested dictionary. Namespace the keys with a period.

    For example, given the following dictionary:

    {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
            }
        }
    }

    it should become:

    {
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
    }

    You can assume keys do not contain dots in them, i.e. no clobbering will occur.
    :return:
    """
    return None


def markov_chain():
    """
    This problem was asked by Google.

You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps
num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.

For example, given the starting state a, number of steps 5000, and the following transition probabilities:

[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]

One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.
    :return:
    """
    return None


def one_to_one_character_mapping():
    """
    This problem was asked by Bloomberg.

    Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

    For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

    Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
    :return:
    """
    return None


def reconstruct_tree():
    """
    This problem was asked by Google.

    Given the sequence of keys visited by a postorder traversal of a binary search tree, reconstruct the tree.

    For example, given the sequence 2, 4, 3, 8, 7, 5, you should construct the following tree:

    5
   / \
  3   7
 / \   \
2   4   8

    :return:
    """
    return None


def interleave():
    """
    This problem was asked by Google.

    Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one
    other queue. This should be done in-place.

    Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

    For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4],
    it should become [1, 4, 2, 3].

    Hint: Try working backwards from the end state.

    :return:
    """
    return None


def rotate_linked_list_k():
    """
    This problem was asked by Airbnb.

    Given a linked list and a positive integer k, rotate the list to the right by k places.

    For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

    Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.
    :return:
    """
    return None


def minimally_connected():
    """
    This problem was asked by Facebook.

    A graph is minimally-connected if it is connected and there is no edge that can be removed while still leaving the
    graph connected. For example, any binary tree is minimally-connected.

    Given an undirected graph, check if the graph is minimally-connected. You can choose to represent the graph as
    either an adjacency matrix or adjacency list.
    :return:
    """
    return None


def greatest_common_denominator():
    """
    This problem was asked by Amazon.

    Given n numbers, find the greatest common denominator between them.

    For example, given the numbers [42, 56, 14], return 14.
    :return:
    """
    return None


def area_of_intersection():
    """
    This problem was asked by Google.

    Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect,
    return 0.

    For example, given the following rectangles:

    {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
    }

    and

    {
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
    }

    return 6.
    :return:
    """
    return None


def smallest_difference_subsets():
    """
    This problem was asked by Microsoft.

    Given an array of positive integers, divide the array into two subsets such that the difference between the sum of
    the subsets is as small as possible.

    For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5,
    which is the smallest possible difference.
    :return:
    """
    return None


def overlapping_rectangles():
    """
    This problem was asked by Google.

    You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a
    pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.

    For example, given the following rectangles:

    {
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
    },
    {
    "top_left": (-1, 3),
    "dimensions": (2, 1)
    },
    {
    "top_left": (0, 5),
    "dimensions": (4, 3)
    }

    :return:
    """
    return None


def max_sub_array_sum():
    """
    This problem was asked by Facebook.

    Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case
    the sum is 0.

    For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from
    wrapping around.

    Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
    :return:
    """
    return None


def minimum_non_overlapping_intervals():
    """
    This problem was asked by Stripe.

    Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
    intervals non-overlapping.

    Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

    For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the
    first two won't overlap.

    The intervals are not necessarily sorted in any order.
    :return:
    """
    return None


def smaller_large():
    """
    This problem was asked by Google.

    Let A be an N by M matrix in which every row and every column is sorted.

    Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

    For example, given the following matrix:

    [[1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]]

    And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or
    greater than 23.
    :return:
    """
    return None


def frequent_subtree_sum():
    """
    This problem was asked by Apple.

    Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.

    For example, given the following tree:

         5
        / \
       2  -5

    Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.
    :return:
    """
    return None


def balanced_string():
    """
    This problem was asked by Facebook.

    Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of
    insertions and deletions. If there are multiple solutions, return any of them.

    For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
    :return:
    """
    return None


def smallest_set_points():
    """
    This problem was asked by Microsoft.

    Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X if every interval in X
    contains at least one point in P. Compute the smallest set of points that stabs X.

    For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9].

    :return:
    """
    return None


def weight_max_path():
    """
    This problem was asked by Google.

    You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers.
    For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

     1
    2 3
   1 5 1

    We define a path in the triangle to start at the top and go down one row at a time to an adjacent value,
    eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum
    of the entries.

    Write a program that returns the weight of the maximum weight path.

    :return:
    """
    return None


def palindrome_integer():
    """
    This problem was asked by Palantir.

    Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888.
    678 is not a palindrome. Do not convert the integer into a string
    :return:
    """
    return None


def minimum_element_log_time():
    """
    This problem was asked by Uber.

    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
    Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

    For example, given [5, 7, 10, 3, 4], return 3.
    :return:
    """
    return None


def count_nodes_faster():
    """
    This problem was asked by Amazon.

    Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree
    has every level filled except the last, and the nodes in the last level are filled starting from the left.
    :return:
    """
    return None


def next_permutation():
    """
    This problem was asked by IBM.

    Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next
    permutation would be 49578.
    :return:
    """
    return None


def permutation_to_array():
    """
    This problem was asked by Twitter.

    A permutation can be specified by an array P, where P[i] represents the location of the element at i in the
    permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

    Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"]
    and the permutation [2, 1, 0], return ["c", "b", "a"].
    :return:
    """
    return None


def partition_linked_list():
    """
    This problem was asked by LinkedIn.

    Given a linked list of numbers and a pivot k, partition the linked list so that all nodes less than k come before
    nodes greater than or equal to k.

    For example, given the linked list 5 -> 1 -> 8 -> 0 -> 3 and k = 3, the solution could be 1 -> 0 -> 5 -> 8 -> 3.
    :return:
    """
    return None


def length_longest_common_subsequence():
    """
    This problem was asked by YouTube.

    Write a program that computes the length of the longest common subsequence of three given strings.
    For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious", it should return 5,
    since the longest common subsequence is "eieio".
    :return:
    """
    return None


def collatz_sequence():
    """
    A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

    if n is even, the next number in the sequence is n / 2
    if n is odd, the next number in the sequence is 3n + 1

    It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

    Bonus: What input n <= 1000000 gives the longest sequence?
    :return:
    """
    return None


def starting_indices_of_occurrences():
    """
    This problem was asked by Microsoft.

    Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string.
    For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
    :return:
    """
    return None


def length_longest_consecutive_run():
    """
    This problem was asked by Stripe.

    Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

    For example, given 156, you should return 3.
    :return:
    """
    return None


def tree_bottom_view():
    """
    This problem was asked by Yelp.

    The horizontal distance of a binary tree node describes how far left or right the node will be when the
    tree is printed out.

More rigorously, we can define it as follows:

    The horizontal distance of the root is 0.
    The horizontal distance of a left child is hd(parent) - 1.
    The horizontal distance of a right child is hd(parent) + 1.

For example, for the following tree, hd(1) = -2, and hd(6) = 0.

             5
          /     \
        3         7
      /  \      /   \
    1     4    6     9
   /                /
  0                8

The bottom view of a tree, then, consists of the lowest node at each horizontal distance.
If there are two nodes at the same depth and horizontal distance, either is acceptable.

For this tree, for example, the bottom view could be [0, 1, 3, 6, 8, 9].

Given the root to a binary tree, return its bottom view.
    :return:
    """
    return None


def convert_roman_numeral():
    """
    This problem was asked by Facebook.

    Given a number in Roman numeral format, convert it to decimal.

    The values of Roman numerals are as follows:

    {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
    }

    In addition, note that the Roman numeral system uses subtractive notation for numbers such as IV and XL.

    For the input XIV, for instance, you should return 14.
    :return:
    """
    return None


def smallest_sparce_number():
    """
    This problem was asked by Oracle.

    We say a number is sparse if there are no adjacent ones in its binary representation. For example, 21 (10101) is
    sparse, but 22 (10110) is not. For a given input N, find the smallest sparse number greater than or equal to N.

    Do this in faster than O(N log N) time.
    :return:
    """
    return None


def reverse_directed_graph():
    """
    This problem was asked by Yahoo.

    Write an algorithm that computes the reversal of a directed graph. For example, if a graph consists of
    A -> B -> C, it should become A <- B <- C.
    :return:
    """
    return None


def connect_4():
    """
    This problem was asked by Salesforce.

    Connect 4 is a game where opponents take turns dropping red or black discs into a 7 x 6 vertically suspended grid.
    The game ends either when one player creates a line of four consecutive discs of their color
    (horizontally, vertically, or diagonally), or when there are no more spots left in the grid.

    Design and implement Connect 4.
    :return:
    """
    return None


def maximum_win():
    """
    This problem was asked by Square.

    In front of you is a row of N coins, with values v1, v1, ..., vn.

    You are asked to play the following game. You and an opponent take turns choosing either the first or last coin
    from the row, removing it from the row, and receiving the value of the coin.

    Write a program that returns the maximum amount of money you can win with certainty, if you move first,
    assuming your opponent plays optimally.
    :return:
    """
    return None


def find_sevenish_number():
    """
    This problem was asked by Zillow.

    Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7.
    The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
    :return:
    """
    return None


def shortest_standardized_path():
    """
    This problem was asked by Quora.

    Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

    For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
    :return:
    """
    return None


def in_order_transversal():
    """
    This problem was asked by Palantir.

    Typically, an implementation of in-order traversal of a binary tree has O(h) space complexity,
    where h is the height of the tree. Write a program to compute the in-order traversal of a binary tree
    using O(1) space
    :return:
    """
    return None


def smallest_positive_integer_not_sum_of_array_subset():
    """
    This problem was asked by Amazon.

    Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

    For example, for the input [1, 2, 3, 10], you should return 7.

    Do this in O(N) time.
    :return:
    """
    return None


def last_survivor():
    """
    This problem was asked by Bloomberg.

    There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with
    the kth person, and removing every successive kth person going clockwise until there is no one left.

    Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

    For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

    Bonus: Find an O(log N) solution if k = 2.
    :return:
    """
    return None


def correct_order_of_letters():
    """
    This problem was asked by Airbnb.

    You come across a dictionary of sorted words in a language you've never seen before. Write a program that returns
    the correct order of letters in this language.

    For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].
    :return:
    """
    return None


def boggle_solver():
    """
    This problem was asked by Facebook.

    Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be
    formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and
    a dictionary of valid words, implement a Boggle solver.
    :return:
    """
    return None


def rearrange_to_largest_possible_integer():
    """
    This problem was asked by Twitter.

    Given a list of numbers, create an algorithm that arranges them in order to form the largest possible integer.
    For example, given [10, 7, 76, 415], you should return 77641510.
    :return:
    """
    return None


def egg_break_floor():
    """
    This problem was asked by Goldman Sachs.

    You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor
    that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again.
    If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor
    greater than x.

    Write an algorithm that finds the minimum number of trial drops it will take, in the worst case,
    to identify this floor.

    For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first,
    until we reach the fifth floor, so our solution will be 5.
    :return:
    """
    return None


def rearrange_string():
    """
    This problem was asked by IBM.

    Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same.
    If this is not possible, return None.

    For example, given "aaabbc", you could return "ababac". Given "aaab", return None.
    :return:
    """
    return None


def fib(n):
    """
    This problem was asked by Apple.

    Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.
    """
    return None