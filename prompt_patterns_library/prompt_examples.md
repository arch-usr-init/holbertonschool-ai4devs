# Prompt Testing Examples

This document contains five tested prompt examples demonstrating different prompt engineering techniques for software development. Each example includes a role, task description, filled input placeholder, expected output format, AI output, and feedback.

---

## Example 1 – Code Refactoring Prompt

**Prompt Used:**

Act as a Senior Python Developer.

**Role:** Senior Python Developer.

**Task Description:** Refactor the provided Python function to improve readability while preserving its original behavior. Use meaningful variable names and proper formatting.

**Input Placeholder:** `{code}`

**Filled Input:** 
```python
def calc(a,b):
    return a+b*10
```

**Expected Output Format:** A refactored Python code block with meaningful function and parameter names.

**Input Provided:**
```python
def calc(a,b):
    return a+b*10
```

**AI Output:**
```python
def calculate_total(first_number, second_number):
    return first_number + (second_number * 10)
```

**Feedback:** The output improves readability through meaningful parameter names and proper formatting. The original mathematical behavior is preserved because multiplication is performed before addition.

---

## Example 2 – Code Explanation Prompt

**Prompt Used:**

Act as an Experienced Python Developer and Technical Instructor.

**Role:** Experienced Python Developer and Technical Instructor.

**Task Description:** Explain the provided Python code in simple terms for a beginner. Describe what each important operation does.

**Input Placeholder:** `{code}`

**Filled Input:**
```python
numbers = [2, 4, 6, 8]
result = sum(numbers)
print(result)
```

**Expected Output Format:** A beginner-friendly explanation followed by the program's output.

**Input Provided:**
```python
numbers = [2, 4, 6, 8]
result = sum(numbers)
print(result)
```

**AI Output:**

The code creates a list containing four numbers: 2, 4, 6, and 8.

The `sum()` function adds all the numbers together and stores the result in the variable `result`.

Finally, `print(result)` displays the result.

Output:
```text
20
```

**Feedback:** The explanation is accurate and beginner-friendly. It describes the list, the sum function, and the print statement clearly without unnecessary technical details.

---

## Example 3 – Bug Detection Prompt

**Prompt Used:**

Act as a Python Debugging Specialist.

**Role:** Python Debugging Specialist.

**Task Description:** Analyze the provided Python code, identify the programming error, explain why it happens, and provide a corrected version.

**Input Placeholder:** `{code}`

**Filled Input:**
```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers) + 1):
    print(numbers[i])
```

**Expected Output Format:** A short explanation of the error followed by corrected Python code.

**Input Provided:**
```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers) + 1):
    print(numbers[i])
```

**AI Output:**

The problem is an off-by-one error.

The list contains five elements, with indexes ranging from 0 to 4. However, `range(len(numbers) + 1)` also generates index 5, which does not exist.

This causes an `IndexError`.

Corrected code:
```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
```

**Feedback:** The AI correctly identifies the off-by-one error, explains why it occurs, and provides a working correction. The explanation is clear and technically accurate.

---

## Example 4 – Code Documentation Prompt

**Prompt Used:**

Act as a Professional Python Developer and Code Documentation Specialist.

**Role:** Professional Python Developer and Code Documentation Specialist.

**Task Description:** Generate a descriptive Python docstring for the provided function. Include its purpose, parameters, and return value without changing the function's implementation.

**Input Placeholder:** `{code}`

**Filled Input:**
```python
def multiply(a, b):
    return a * b
```

**Expected Output Format:** Python code containing the original function and a properly formatted docstring.

**Input Provided:**
```python
def multiply(a, b):
    return a * b
```

**AI Output:**
```python
def multiply(a, b):
    """
    Multiply two numbers and return their product.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b
```

**Feedback:** The generated docstring clearly explains the function's purpose, parameters, and return value. The original implementation remains unchanged.

---

## Example 5 – Code Generation Prompt

**Prompt Used:**

Act as an Experienced Python Software Developer.

**Role:** Experienced Python Software Developer.

**Task Description:** Create a Python function that determines whether an integer is even or odd. Use an if-else statement and the modulo operator. Include simple test cases.

**Input Placeholder:** `{requirements}`

**Filled Input:** Create a function that accepts an integer and returns either "Even" or "Odd".

**Expected Output Format:** A complete Python code block containing the function and two test cases, followed by their expected output.

**Input Provided:** Create a function that accepts an integer and returns either "Even" or "Odd".

**AI Output:**
```python
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(4))
print(check_even_odd(7))
```

Output:
```text
Even
Odd
```

**Feedback:** The generated function correctly uses the modulo operator to determine whether a number is even or odd. Both test cases demonstrate the expected behavior. The implementation is simple and readable.

---

## Conclusion

Five prompt patterns were evaluated using practical Python programming examples.

1. Code Refactoring – improving code readability and maintainability.
2. Code Explanation – making existing code easier to understand.
3. Bug Detection – identifying and correcting programming errors.
4. Code Documentation – generating descriptive docstrings.
5. Code Generation – creating code from natural-language requirements.

These examples demonstrate how structured prompts containing explicit roles, task descriptions, input placeholders, and expected output formats can improve the clarity and consistency of AI-generated programming assistance.
