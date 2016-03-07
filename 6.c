// PROBLEM 6
// The sum of the squares of the first ten natural numbers is,
//              1^2 + 2^2 + ... + 10^2 = 385
// The square of the sum of the first ten natural numbers is,
//              (1 + 2 + ... + 10)^2 = 55^2 = 3025
// Hence the difference between the sum of the squares of the first
// ten natural numbers and the square of the sum is
//              3025 − 385 = 2640.
// Find the difference between the sum of the squares of the first
// one hundred natural numbers and the square of the sum.

#include <stdio.h>

int main(int argc, char *argv[]) {
    int i;
    long sum = 0L;
    long sum_sq = 0L;
    for (i = 0; i <= 100; ++i) {
        sum = sum+i;
        sum_sq = i*i + sum_sq;
    }
    int sq_sum = sum*sum;
    printf("1**2 + 2**2 + 3**2 ... 100**2 = %d\n", sq_sum);
    printf("(1+2+3...100)**2 = %lu\n", sum_sq);
    printf("%lu\n", sq_sum-sum_sq);
    return 0;
}
