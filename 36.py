# Problem 36

# The decimal number, 585 = 10010010012 (binary), is palindromic
# in both bases.

# Find the sum of all numbers, less than one million,
# which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base,
# may not include leading zeros.)

def main():
    sum = 0
    for i in xrange(0,1000000):
        bin_i = bin(i)[2:]
        if bin_i == bin_i[::-1] and str(i) == str(i)[::-1]:
            sum += i
    print sum

if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
