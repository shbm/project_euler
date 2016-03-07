#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sieve(n):
    is_prime = [False] * 2 + [True] * (n - 1) 
    for i in xrange(int(n**0.5 + 1.5)): # stop at ``sqrt(n)``
        if is_prime[i]:
            for j in xrange(i*i, n+1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

def main():
    try:
        primes =  sieve(1000000)
        for i in primes:
            i
        print len(primes)
        print "10001", primes[10000]
    except ValueError:
        print 'Enter only an integer value, n > 1.'
        main()

if __name__ == '__main__':
    main()
