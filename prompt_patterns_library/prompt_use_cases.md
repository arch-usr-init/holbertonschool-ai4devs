# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve code readability, maintainability, and performance without changing existing behavior.
  - **Input**: Source code of a function or module in [LANGUAGE].
  - **Output**: Refactored code with an explanation of the improvements.

- **Style Enforcement**
  - **Goal**: Apply consistent naming conventions, formatting, and coding standards.
  - **Input**: A code block and the required style guidelines.
  - **Output**: Revised code that follows the specified coding standards.

- **Code Review**
  - **Goal**: Identify code smells, unnecessary complexity, and potential quality issues.
  - **Input**: Source code of a function, class, or module.
  - **Output**: Code review findings with recommended improvements and examples.

## Debugging

- **Error Diagnosis**
  - **Goal**: Identify the root cause of a runtime error or unexpected behavior.
  - **Input**: Error message, relevant source code, and steps to reproduce the issue.
  - **Output**: Explanation of the root cause and a proposed fix.

- **Bug Fixing**
  - **Goal**: Correct a specific defect while preserving existing functionality.
  - **Input**: Bug description, affected source code, and expected behavior.
  - **Output**: Corrected code with an explanation of the changes.

- **Edge Case Detection**
  - **Goal**: Discover unexpected inputs and boundary conditions that could cause failures.
  - **Input**: Function or module source code and its intended behavior.
  - **Output**: List of potential edge cases with examples and suggested handling strategies.

## Documentation

- **Function Documentation**
  - **Goal**: Generate clear documentation explaining a function's purpose, parameters, and return values.
  - **Input**: Source code of a function in [LANGUAGE].
  - **Output**: Documentation with a description, parameter details, return values, and usage examples.

- **README Generation**
  - **Goal**: Create understandable project documentation for developers and contributors.
  - **Input**: Project structure, purpose, installation instructions, and usage information.
  - **Output**: A structured README.md containing project overview, setup steps, and usage examples.

- **Code Explanation**
  - **Goal**: Make complex code easier to understand for developers.
  - **Input**: A source code block or module.
  - **Output**: A step-by-step explanation of its logic, components, and execution flow.

## Testing

- **Unit Test Generation**
  - **Goal**: Create automated tests that verify individual functions or components.
  - **Input**: Function source code, expected behavior, and testing framework.
  - **Output**: Unit tests covering normal inputs, edge cases, and expected outputs.

- **Test Case Generation**
  - **Goal**: Identify different scenarios to validate application behavior.
  - **Input**: Feature requirements, acceptance criteria, or function specifications.
  - **Output**: A categorized set of test cases with inputs, expected results, and descriptions.

- **Test Failure Analysis**
  - **Goal**: Diagnose failing tests and determine whether the problem is in the implementation or the tests.
  - **Input**: Test code, failure output, and relevant application source code.
  - **Output**: Explanation of the failure and recommended corrections.
