# Reflection on Prompt Design

## Introduction

The Prompt Patterns Library project helped me understand that writing an effective prompt is more than asking an AI tool a question. A useful prompt gives the model enough context to understand the task, the information it should work with, and the form of the response expected. The goal of this project was to create reusable templates for common software development activities, organize them into categories, and examine how their structure affects the results. Building and documenting the library showed me that a prompt should be clear enough to reuse, but flexible enough to work with different inputs.

## Easy vs Hard Prompt Types

Some prompt types were easier to generalize than others. Code explanation and documentation prompts were relatively straightforward because their expected tasks are familiar and consistent. For example, a template can ask the AI to explain a code snippet for a beginner or write a docstring describing a function's purpose, parameters, and return value. The input changes from one example to another, but the overall instructions remain similar.

Refactoring and code generation were also reusable, although they need more careful constraints. A refactoring prompt should preserve existing behavior, while a code generation prompt must define the required behavior and relevant edge cases. Debugging was the hardest type to generalize. Different bugs can have very different causes, and a useful diagnosis may require the error message, expected behavior, actual behavior, and surrounding code. A broad instruction such as "find the bug" may not provide enough context for a reliable answer.

## Key Elements

The project highlighted three important structural elements: role, tone, and input placeholders. A role, such as "Act as a Python debugging specialist," establishes the perspective and level of expertise expected from the model. Tone helps control how the answer is communicated. For example, asking for a beginner-friendly explanation encourages simpler language, while asking for a concise technical review suits a developer audience.

Placeholders make templates reusable. A placeholder such as `{code}`, `{error_message}`, or `{requirements}` shows exactly which information should be supplied by the user. Clear placeholders also reduce ambiguity. I learned that placeholders should be specific rather than overly general; `{code}` and `{expected_behavior}` are more useful than one vague `{input}` field when debugging.

## Impact on Output

Prompt structure directly influences the relevance, consistency, and usefulness of the output. For example, asking "Explain this code" may produce an explanation with an unpredictable level of detail. Adding a role and audience—"Act as a Python instructor and explain this code to a beginner"—gives the model clearer direction. Similarly, a refactoring prompt that explicitly says to preserve behavior is safer and more useful than simply asking the model to make code cleaner.

Output-format instructions also improve usability. Requesting a corrected code block followed by a short explanation makes a debugging response easier to review. However, structure does not guarantee correctness. A prompt can be detailed and still receive an incorrect answer, so generated code and explanations should be checked, including with appropriate tests. This is an important limitation of prompt engineering.

## Future Work

The library could be improved by documenting each template's purpose, required inputs, optional inputs, constraints, and expected output format in a consistent format. I would also add examples for different programming languages and difficulty levels, plus edge cases that test whether a template works beyond a simple example. Each template could include a short checklist for reviewing the AI response, such as correctness, completeness, readability, and whether the requested format was followed.

Finally, I would keep a record of test inputs, actual model outputs, and revisions to each template. Comparing results across several examples would make it easier to identify weaknesses and improve prompts systematically. Overall, this project taught me that effective prompt patterns are not just well-written instructions: they are reusable specifications that guide an AI system while still requiring human review.
