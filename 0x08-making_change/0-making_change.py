#!/usr/bin/python3
"""
Module for making change using different coin denominations
"""

def makeChange(coins, total):
    """
    Determines the least number of coins needed to meet a given total.

    Args:
        coins (list): List of coin denominations.
        total (int): The target total amount.

    Returns:
        int: least number of coins needed to meet the total amount.
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1

    try:
        x = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_sum = 0
    for i in coins:
        if total % i == 0:
            coin_sum += int(total / i)
            return coin_sum
        if total - i >= 0:
            if int(total / i) > 1:
                coin_sum += int(total / i)
                total = total % i
            else:
                coin_sum += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return coin_sum
