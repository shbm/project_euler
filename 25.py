# PROBLEM 25

# The Fibonacci sequence is defined by the recurrence relation:

# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:

        # F1 = 1
        # F2 = 1
        # F3 = 2
        # F4 = 3
        # F5 = 5
        # F6 = 8
        # F7 = 13
        # F8 = 21
        # F9 = 34
        # F10 = 55
        # F11 = 89
        # F12 = 144
        # The 12th term, F12, is the first term
        # to contain three digits.

# What is the index of the first term in the
# Fibonacci sequence to contain 1000 digits?

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib = memoize(fib)

def main():
    for i in xrange(10000):
        x = len(str(fib(i)))
        if x > 999:
            print i
            print fib(i)
            break

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
