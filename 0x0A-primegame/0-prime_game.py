#!/usr/bin/python3
"""
This module contains the function isWinner that returns the name of the player
that won the most rounds in the game.
"""


def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.

    Args:
        n (int): number to be checked

    Returns:
        bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False

    i = 2
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def isWinner(x, nums):
    """
    Returns the name of the player that won the most rounds in the game.

    Args:
        x (int): number of rounds
        nums (list): list of integers representing a round

    Returns:
        str: name of the player that won the most rounds in the game
    """
    players = {'Maria': 0, 'Ben': 0}
    for round in range(x):
        n = nums[round]

        # even numbers for Maria & odd numbers for Ben
        winner = 1
        i = 2
        while i <= n:
            while (i <= n + 1) and (not is_prime(i)):
                i += 1
            # no prime numbers left
            if i > n:
                break
            winner += 1  # change current winner
            i += 1

        # validate winner
        if winner % 2 == 0:
            players['Maria'] += 1
        else:
            players['Ben'] += 1

    # return who won most rounds
    if players['Ben'] < players['Maria']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
