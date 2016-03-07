#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Efficitent solution for Problem 14 in project Euler

# collatz_cache = {1: 1}

# def collatz_chain_length(x):
    # if x not in collatz_cache:
        # if x % 2 == 0:
            # y = x // 2
        # else:
            # y = x * 3 + 1
        # collatz_cache[x] = collatz_chain_length(y) + 1
    # return collatz_cache[x]

# try:
    # print collatz_chain_length(837799)
# except RuntimeError:
    # pass
# print collatz_cache

def cc(x):
    counter = 0
    if x == 1:
        counter += 1
        return counter
    else:
        if x%2 == 0:
            y = x/2
            counter += 1
        else:
            y = 3*x+1
            counter += 1
        cc(y)

print cc(10)
