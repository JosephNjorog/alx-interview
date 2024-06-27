# README

## Project: 0x00. Pascal's Triangle

### Introduction
Pascal's Triangle is a triangular array of binomial coefficients. Each row represents the coefficients of the binomial expansion. This project involves implementing a function to generate Pascal's Triangle up to a given number of rows `n`. The function should return a list of lists, where each inner list represents a row of the triangle.

### Must Know Concepts

To successfully complete this project, you should have a solid understanding of the following Python concepts:

#### Lists and List Comprehensions
- **Creating and Accessing Lists:** Know how to create lists, access elements using indexing, and modify elements.
- **Iterating Over Lists:** Use loops to iterate through lists.
- **List Comprehensions:** Utilize list comprehensions for concise and readable code, especially for generating rows of Pascal’s Triangle.

#### Functions
- **Defining Functions:** Understand how to define functions using the `def` keyword.
- **Calling Functions:** Know how to call functions and pass arguments to them.
- **Returning Values:** Be able to return values from functions, particularly lists of lists representing Pascal’s Triangle.

#### Loops
- **For Loops:** Use for loops to iterate over sequences and generate rows of the triangle.
- **While Loops:** Understand the use of while loops, though for loops are more suited for this task.
- **Nested Loops:** Use nested loops to handle the creation of each row and the calculation of its values.

#### Conditional Statements
- **If, Elif, and Else:** Apply conditional statements to handle different cases, such as the edges of the triangle always being 1.

#### Recursion (Optional)
- **Base Cases and Recursive Cases:** Recognize how to implement recursive functions to generate Pascal’s Triangle. This is an optional approach and not strictly necessary.

#### Arithmetic Operations
- **Addition:** Perform addition operations to calculate each element of Pascal’s Triangle as the sum of the two elements directly above it.

#### Indexing and Slicing
- **Accessing Elements:** Use indexing to access specific elements in a list.
- **Slicing Lists:** Use slicing to obtain sublists when necessary.

#### Memory Management
- **List Storage and Copying:** Be mindful of how lists are stored and copied. Understand the difference between shallow and deep copies.

#### Error and Exception Handling (Optional)
- **Try-Except Blocks:** Use try-except blocks to handle potential errors such as invalid input types or values.

#### Efficiency and Optimization
- **Time and Space Complexity:** Consider the efficiency of different approaches to generating Pascal’s Triangle. Optimize your solution to improve performance.

### Task Description

#### Task 0: Pascal's Triangle
**Objective:** Create a function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s Triangle of `n`.

**Steps:**
1. **Function Definition:** Define the function `pascal_triangle(n)`.
2. **Input Validation:** Check if `n` is less than or equal to 0. If so, return an empty list.
3. **Initialize Triangle:** Start with an initial list containing the first row `[1]`.
4. **Generate Rows:** Use loops to generate each row of the triangle.
   - Each element in a row (except the first and last) is the sum of the two elements directly above it from the previous row.
5. **Return Result:** Return the list of lists representing Pascal’s Triangle.

**Outcome:**
- The function generates Pascal's Triangle correctly for any positive integer `n`.
- For `n <= 0`, the function returns an empty list.

### Example Usage

```python
if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

**Expected Output:**

```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

### Conclusion
By revisiting and mastering the above concepts, you will be well-prepared to implement an efficient solution for generating Pascal’s Triangle in Python. This project will enhance your understanding of fundamental programming concepts and improve your problem-solving skills in algorithmic tasks.
