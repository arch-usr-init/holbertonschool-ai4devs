# Bug Snippets — Intended Behavior

This collection contains five deliberately broken programs for AI-assisted debugging. Each sample is 10–40 lines long. Keep the original files unchanged for the initial debugging exercise; corrected versions will be documented separately in later tasks.

## Bug 1 — `bug1.py`
- **Language:** Python
- **Issue Type:** Syntax error
- **Intended Behavior:** Read a comma-separated list of integers, ignore zero and negative values, and print the sum of positive values. For `"3, -2, 5, 0"`, the expected sum is `8`.
- **Observed Symptom:** Python rejects the file before it can run because of invalid statement syntax.

## Bug 2 — `bug2.py`
- **Language:** Python
- **Issue Type:** Logical error
- **Intended Behavior:** Apply a 10% discount to `[100.0, 50.0, 30.0]` and print `[90.0, 45.0, 27.0]`.
- **Observed Symptom:** The program runs, but its calculated prices increase instead of decreasing.

## Bug 3 — `bug3.js`
- **Language:** JavaScript (Node.js)
- **Issue Type:** Runtime exception
- **Intended Behavior:** Return the names of users with `score >= 70`, preserving input order. Expected names are `Ada` and `Lin`.
- **Observed Symptom:** Accessing a missing nested property throws a `TypeError` during execution.

## Bug 4 — `bug4.js`
- **Language:** JavaScript (Node.js)
- **Issue Type:** Off-by-one / loop boundary
- **Intended Behavior:** Return the last `3` elements of `[10, 20, 30, 40, 50]` as `[30, 40, 50]`.
- **Observed Symptom:** Only two items are returned.

## Bug 5 — `bug5.cpp`
- **Language:** C++
- **Issue Type:** Data type misuse / integer division
- **Intended Behavior:** Compute the floating-point arithmetic mean of integer scores `[4, 4, 5]`, approximately `4.33333`.
- **Observed Symptom:** The code compiles but prints an integer-valued average because of arithmetic conversion rules.

## Suggested Reproduction Commands

```bash
python bug1.py              # Expected to fail during parsing
python bug2.py              # Incorrect numerical result
node bug3.js                # Expected to throw a TypeError
node bug4.js                # Incorrect array length
c++ -std=c++17 bug5.cpp -o bug5 && ./bug5  # Incorrect numerical result
```

**Important:** Errors are intentional. Do not correct the original snippets before recording the initial AI debugging attempts.
