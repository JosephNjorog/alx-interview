# 0x01. Lockboxes

## Overview

In this project, I developed a solution to determine if all lockboxes can be unlocked given a set of keys contained within the boxes. This README provides a detailed step-by-step explanation of the tasks I completed and the methods I used.

## Learning Objectives

By the end of this project, I was able to:

- Work with lists and understand list manipulation in Python.
- Understand and apply graph theory concepts, particularly traversal algorithms like DFS.
- Analyze algorithmic complexity.
- Implement recursion in Python.
- Use queues and stacks for algorithm implementation.
- Utilize set operations to optimize search processes.

## Requirements

- Allowed editors: vi, vim, emacs
- All files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All files ended with a new line
- The first line of all files was exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder
- Code documentation
- PEP 8 style compliance (version 1.7.x)
- All files were executable

## Task 0: Lockboxes

### Objective

The main objective was to write a method that determines if all the boxes can be opened. 

### Method Prototype

```python
def canUnlockAll(boxes)
```

### Requirements

- `boxes` is a list of lists.
- A key with the same number as a box opens that box.
- All keys are positive integers.
- Some keys may not have corresponding boxes.
- The first box `boxes[0]` is unlocked.
- Return `True` if all boxes can be opened, else return `False`.

### Approach

1. **Initialization**: Start with the first box (which is already unlocked) and initialize a set to keep track of unlocked boxes.
2. **Queue Setup**: Use a queue to manage the boxes to be processed. Initially, add the first box to the queue.
3. **Process Boxes**: 
   - While there are boxes in the queue, get the keys from the current box.
   - For each key, if it opens a box that hasn't been opened yet, add that box to the set of unlocked boxes and to the queue for further processing.
4. **Check Completion**: After processing all possible boxes, check if the number of unlocked boxes is equal to the total number of boxes.

### Implementation

Here is the implementation of the `canUnlockAll` method:

```python
def canUnlockAll(boxes):
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
```

### Usage

To test the `canUnlockAll` function, I used the following script:

```python
#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # Output: False
```

## Repository

The code for this project is available in the following repository:

- **GitHub repository**: alx-interview
- **Directory**: 0x01-lockboxes
- **File**: 0-lockboxes.py

## Conclusion

Through this project, I successfully implemented a method to determine if all boxes can be unlocked using a combination of list manipulation, set operations, and graph traversal algorithms. This project helped me strengthen my understanding of Python programming and algorithmic problem-solving.
