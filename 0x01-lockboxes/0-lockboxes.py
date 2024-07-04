#!/usr/bin/python3
"""
This module contains a function to solve the lockboxes algorithm problem
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list): list of boxes

    Return:
        (bool) True if all boxes can be opened, false otherwise
    """
    if not boxes:
        return False

    unlocked = set()
    unlocked.add(0)
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == len(boxes)
