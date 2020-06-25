#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------


def collatz_read(s):
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    if len(a) > 1:
        if a[0].isdigit() and a[1].isdigit():
            return [int(a[0]), int(a[1])]
        else:
            return [0, 0]
    else:
        if a[0].isdigit():
            return [int(a[0]), 0]
        return [0, 0]

# ------------
# collatz_eval
# ------------


def collatz_eval(i, j):
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    memo = []
    return recursive_max(memo, i, j, 0)

def recursive_max(i, j, max):
    if i <= 0 or j <= 0:
        return 0
    num = i
    count = 1
    while num > 1:
        if num in memo:
            break
        else:
            memo.append(num)
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        count += 1
    if count > max:
        max = count
    if i == j:
        return max
    if i < j:
        return recursive_max(memo, i + 1, j, max)
    if i > j:
        return recursive_max(memo, i - 1, j, max)

# -------------
# collatz_print
# -------------


def collatz_print(w, i, j, v):
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    r a reader
    w a writer
    """
    for s in r:
        i, j = collatz_read(s)
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
