#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to reach exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    operations, divisor = 0, 2
    while divisor <= n:
        # if n evenly divides by divisor
        if n % divisor == 0:
            # total even-divisions by divisor = total operations
            operations += divisor
            # set n to the remainder
            n = n / divisor
            # reduce divisor to find remaining smaller vals that evenly-divide n
            divisor -= 1
        # increment divisor until it evenly-divides n
        divisor += 1
    return operations
