# Benchmark Tasks - Copilot Productivity Sprint

## Task 1 - Word Frequency Counter
**Requirements**: Write a function `get_top_words(text, n)` that takes a string of text and an integer `n`, and returns the top `n` most frequently occurring words. The function must ignore case and strip punctuation. 
**Inputs**: 
- `text` (String): A paragraph of text.
- `n` (Integer): The number of top words to return.
**Outputs**: A list of tuples containing the word and its count, sorted in descending order by count. Example: `[("the", 5), ("and", 3)]`
**Acceptance Criteria**:
- Must handle empty strings (returns an empty list).
- Must ignore punctuation (e.g., "hello," and "hello" count as the same word).
- Must be case-insensitive (e.g., "The" and "the" count as the same word).
- Returns exactly `n` items unless there are fewer unique words in the text.

## Task 2 - User Registration Validator
**Requirements**: Implement a function `validate_registration(data)` that checks if a dictionary containing user registration data is valid before saving it to a database.
**Inputs**: A JSON object/Dictionary: `{"username": "string", "email": "string", "password": "string"}`
**Outputs**: A tuple containing a boolean and a list of error strings `(is_valid, errors)`. Example: `(False, ["Invalid email format", "Password too short"])`
**Acceptance Criteria**:
- All three fields (`username`, `email`, `password`) are required. Return an error for any missing field.
- The `email` must contain an `@` symbol and a `.` in the domain part.
- The `password` must be at least 8 characters long.
- The `username` must not contain spaces.
- If all rules pass, return `(True, [])`.

## Task 3 - CSV Average Calculator
**Requirements**: Write a function `calculate_average_age(csv_data)` that parses a string of CSV data and calculates the average age of the users.
**Inputs**: A multi-line string representing a CSV file containing a header row (name, age) followed by user rows (e.g., Alice, 30; Bob, 25).
**Outputs**: A float representing the average age (e.g., `30.0`), or `None` if the data is invalid or empty.
**Acceptance Criteria**:
- Must correctly skip the header row.
- Must handle invalid age formats (e.g., if a row has `age="unknown"`, ignore that row for the average calculation).
- Returns `None` if there are no valid ages to calculate.
- Rounds the final average to two decimal places.
