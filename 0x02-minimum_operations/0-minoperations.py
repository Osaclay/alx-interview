#!/usr/bin/python3
"""
Minimum Operations
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to reach n 'H' characters in a file.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required. Returns 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while n > 1:
        if n % div == 0:
            operations += div  # Adds the current divisor to the operations count
            n = n // div  # Updates n by dividing it by the current divisor
        else:
            div += 1  # Increments the divisor if n is not divisible by it

    return operations
