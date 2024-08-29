#!/usr/bin/python3
"""
This module contains a function to solve the island perimeter algorithm problem
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
        grid (2D list): contains the water and lands

    Returns:
        (int) perimeter of island if it exists
    """
    permiter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                sides = 4
                if j > 0 and grid[i][j - 1] == 1:
                    sides -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    sides -= 1
                if i > 0 and grid[i - 1][j] == 1:
                    sides -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    sides -= 1
                permiter += sides

    return permiter
