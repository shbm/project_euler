# PROBLEM 14

# The following iterative sequence is defined for the set of
# positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the
# following sequence:

#    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing
# at 1)  contains 10 terms. Although it has not been proved yet
# (Collatz Problem), it is thought that all starting numbers
# finish at 1.

# Which starting number, under one million, produces the
# longest chain?

#!/usr/bin/env python
# -*- coding: utf-8 -*-

cache = {1: 1}

def chain_length(x):
    if x not in cache:
        if x%2 == 0:
            y = x/2
        else:
            y = 3*x + 1
        cache[x] = chain_length(y) + 1
    return cache[x]

a = enumerate(range(1, 1000001))
for i, val in a:
    val = chain_length(i+1)

print a
print max(a)
