# Prompt Patterns Library

## Introduction

The Prompt Patterns Library contains reusable prompt templates for common software development activities. Each template defines a role, a task, the information the user must provide, and the expected response format. This structure makes prompts easier to reuse and helps produce more focused, consistent AI assistance.

## Categories

- **Code quality:** reviewing, refactoring, and enforcing coding conventions.
- **Debugging:** analyzing errors, finding edge cases, and investigating performance.
- **Documentation:** generating docstrings, API documentation, and project README files.
- **Testing:** generating unit tests, mock data, and integration test plans.

## Prompt Templates

### Code Quality
- [Code Review](prompts/code_review.md)
- [Refactoring](prompts/refactoring.md)
- [Style Enforcement](prompts/style_enforcement.md)

### Debugging
- [Error Analysis](prompts/error_analysis.md)
- [Edge Case Identification](prompts/edge_case_identification.md)
- [Performance Profiling](prompts/performance_profiling.md)

### Documentation
- [API Documentation](prompts/api_documentation.md)
- [Docstring Generation](prompts/docstring_generation.md)
- [README File Writing](prompts/readme_file_writing.md)

### Testing
- [Unit Test Generation](prompts/unit_test_generation.md)
- [Mock Data Creation](prompts/mock_data_creation.md)
- [Integration Test Planning](prompts/integration_test_planning.md)

## Supporting Documents
- [Prompt Use Cases](prompt_use_cases.md) describes the goal, input, and expected output for each category.
- [Prompt Testing Examples](prompt_examples.md) contains practical examples and feedback.
- [Project Reflection](reflection.md) records lessons learned about prompt design.

## Project Structure
```text
prompt_patterns_library/
├── README.md
├── prompt_use_cases.md
├── prompt_examples.md
├── reflection.md
└── prompts/
    ├── api_documentation.md
    ├── code_review.md
    ├── docstring_generation.md
    ├── edge_case_identification.md
    ├── error_analysis.md
    ├── integration_test_planning.md
    ├── mock_data_creation.md
    ├── performance_profiling.md
    ├── readme_file_writing.md
    ├── refactoring.md
    ├── style_enforcement.md
    └── unit_test_generation.md
```
