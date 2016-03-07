# PROBLEM 5

# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

k = 20
N = 1
i = 1
check = True
limit = math.sqrt(k)
while p[i] <= k:
    a[i] = 1
    if check:
        if p[i] <= limit:
            a[i] = floor( math.log10(k) / math.log10(p[i]) )
        else:
            check = false
    N = N * p[i] ** a[i]
    i = i + 1

print N
