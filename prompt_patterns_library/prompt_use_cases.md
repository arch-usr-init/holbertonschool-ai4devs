# Prompt Use Cases

## Code Quality

- **Refactoring**
  - **Goal**: Improve readability and maintainability while preserving existing behavior.
  - **Input**: Source code, programming language, and behavior that must remain unchanged.
  - **Expected output**: Refactored code with a concise explanation of improvements.

- **Style Enforcement**
  - **Goal**: Apply consistent naming, formatting, and language-specific coding conventions.
  - **Input**: Code block and required style guide or linting rules.
  - **Expected output**: Revised code that follows the supplied conventions, with a summary of changes.

- **Code Review**
  - **Goal**: Detect defects, anti-patterns, security concerns, and performance or maintainability problems.
  - **Input**: Code snippet or pull-request diff, plus relevant requirements.
  - **Expected output**: Prioritized findings with severity, evidence, and actionable recommendations.

## Debugging

- **Error Analysis**
  - **Goal**: Explain an error and identify its likely root cause.
  - **Input**: Stack trace or error message, relevant code, and reproduction details.
  - **Expected output**: Root-cause analysis and practical resolution steps.

- **Edge Case Identification**
  - **Goal**: Find boundary conditions and unusual inputs that current logic may not handle.
  - **Input**: Function logic, input constraints, and expected behavior.
  - **Expected output**: Uncovered cases with example inputs and suggested handling.

- **Performance Profiling**
  - **Goal**: Locate inefficient execution paths and excessive memory or resource use.
  - **Input**: Relevant code, workload description, and profiling measurements or logs.
  - **Expected output**: Bottleneck analysis, complexity considerations, and measurable optimization suggestions.

## Documentation

- **Docstring Generation**
  - **Goal**: Produce clear, consistent documentation for functions, methods, and classes.
  - **Input**: Function or class definition and target language or documentation convention.
  - **Expected output**: Docstring describing purpose, parameters, return values, exceptions, and relevant examples.

- **README File Writing**
  - **Goal**: Create useful project documentation for developers and contributors.
  - **Input**: Project structure, prerequisites, setup commands, configuration, and usage examples.
  - **Expected output**: Structured README with overview, installation, configuration, usage, and contribution guidance.

- **API Documentation**
  - **Goal**: Document API endpoints and their request and response contracts.
  - **Input**: Route definitions, controller logic, authentication rules, and API version.
  - **Expected output**: OpenAPI-compatible endpoint documentation with methods, parameters, request bodies, and response schemas.

## Testing

- **Unit Test Generation**
  - **Goal**: Create tests that verify individual functions or components.
  - **Input**: Target code, expected behavior, and testing framework.
  - **Expected output**: Runnable tests for normal cases, boundary cases, and expected exceptions.

- **Mock Data Creation**
  - **Goal**: Generate realistic test data that conforms to a schema.
  - **Input**: Database schema or JSON structure, constraints, and desired record count.
  - **Expected output**: Valid sample data in the requested format, including useful value variations.

- **Integration Test Planning**
  - **Goal**: Define tests that verify interactions between connected components or services.
  - **Input**: System architecture, service flows, and integration requirements.
  - **Expected output**: Ordered test plan with preconditions, steps, expected assertions, and cleanup notes.
