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

    # Initialize a list to store the minimum coins needed for each total value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
