#!/usr/bin/python3
"""
This module contains the makeChange function to solve fewest coins problem
"""


def makeChange(coins, total):
    """
    Return fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    elif len(coins) == 0:
        return -1
    coins.sort()
    sum = n_coins = 0
    i = len(coins) - 1
    while sum < total:
        while i > 0 and sum + coins[i] > total:
            i -= 1
        sum += coins[i]
        n_coins += 1
    return n_coins if sum == total else -1
