#!/usr/bin/python3
"""
This module contains a function to solve the lockboxes algorrithm problem
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened

    Args:
        boxes (list): list of boxes

    Return:
        (bool) True if all boxes can be opened, false otherwise
    """
    if not boxes or len(boxes) == 1:
        return True

    current_box = 0
    boxes_keys = {}
    next_box = True

    while next_box:
        boxes_keys[current_box] = True
        for key in boxes[current_box]:
            if key not in boxes_keys.keys():
                boxes_keys[key] = False

        if len(boxes_keys) == len(boxes):
            return True

        next_box = False
        for key, unlocked in boxes_keys.items():
            if (not unlocked) and (key < len(boxes) and key >= 0):
                next_box = True
                current_box = key
                break

    return False
