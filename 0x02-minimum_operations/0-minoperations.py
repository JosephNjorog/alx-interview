#!/usr/bin/python3
"""
This module contains the minOperations function that calculates
the fewest number of operations needed to result in exactly n H
characters in the file.
"""


def next_operation(
                   target: int,
                   operations: int,
                   current_characters: int,
                   add_by: int
                   ) -> int:
    """
    Recursive function to calculate the next operation
    Args:
        target (int): The target number of characters
        operations (int): The number of operations
        current_characters (int): The current number of characters
        add_by (int): The number of characters to add by
    Returns:
        int: The number of operations
    """
    if target == current_characters:
        return operations

    if target % current_characters == 0:
        return next_operation(
                              target,
                              operations + 2,
                              current_characters * 2,
                              current_characters
                              )

    return next_operation(
                          target,
                          operations + 1,
                          current_characters + add_by,
                          add_by
                          )


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations needed to result in
    exactly n H characters in the file.
    Args:
        n (int): The target number of characters
    Returns:
        int: The fewest number of operations needed to result in
            exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    return next_operation(n, 2, 2, 1)
