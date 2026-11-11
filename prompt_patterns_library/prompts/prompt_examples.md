# Prompt Testing Examples

## Example 1 – Code Refactoring Prompt

**Prompt**: Refactor the following Python function for readability while preserving its original behavior. Use meaningful variable names and proper formatting.

**Input**:
```python
def calc(a,b):
    return a+b*10
```

**AI Output**:
```python
def calculate_total(first_number, second_number):
    return first_number + (second_number * 10)
```

**Feedback**: The output improves readability through meaningful function parameter names and proper formatting. The original calculation is preserved.

---

## Example 2 – Code Explanation Prompt

**Prompt**: Act as an experienced Python developer. Explain what the following code does in simple terms for a beginner. Include a short explanation of each important operation.

**Input**:
```python
numbers = [2, 4, 6, 8]
result = sum(numbers)
print(result)
```

**AI Output**:

The code creates a list containing four numbers: 2, 4, 6, and 8.

The `sum()` function adds all the numbers together and stores the result in the variable `result`.

Finally, `print(result)` displays the result:

```text
20
```

**Feedback**: The explanation is accurate, simple, and appropriate for beginners. It explains the purpose of each important operation without unnecessary technical details.

---

## Example 3 – Bug Detection Prompt

**Prompt**: Identify the bug in the following Python code, explain why it occurs, and provide a corrected version.

**Input**:
```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers) + 1):
    print(numbers[i])
```

**AI Output**:

The problem is that the loop attempts to access an index that does not exist.

Python list indexes start at 0, so the valid indexes are 0 through 4. However, `range(len(numbers) + 1)` also generates index 5, causing an `IndexError`.

Corrected code:

```python
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
```

**Feedback**: The AI correctly identified the off-by-one error, explained the cause, and provided a working correction. The explanation makes the bug understandable to a beginner.

---

## Example 4 – Code Documentation Prompt

**Prompt**: Write a clear Python docstring for the following function. Explain its purpose, parameters, and return value.

**Input**:
```python
def multiply(a, b):
    return a * b
```

**AI Output**:
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

**Feedback**: The generated docstring clearly describes the function's purpose, arguments, and return value. It follows a recognizable documentation format and preserves the original implementation.

---

## Example 5 – Code Generation Prompt

**Prompt**: Write a Python function that checks whether a given number is even or odd. Use a function, an if-else statement, and return a string indicating the result. Include a simple test.

**Input**:

Create a function that accepts an integer and returns either "Even" or "Odd".

**AI Output**:
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

**Feedback**: The generated function correctly uses the modulo operator to determine whether a number is even or odd. Both test cases demonstrate the expected behavior. The code is simple and easy to understand.

---

## Conclusion

The five prompt templates were evaluated using practical Python programming examples.

The tests demonstrate five useful prompt-engineering applications:

1. Code Refactoring – improving code readability.
2. Code Explanation – understanding existing code.
3. Bug Detection – identifying and correcting programming errors.
4. Code Documentation – generating meaningful docstrings.
5. Code Generation – creating code from natural-language requirements.

These examples demonstrate how structured prompts can help improve the quality, clarity, and usefulness of AI-generated programming assistance.
