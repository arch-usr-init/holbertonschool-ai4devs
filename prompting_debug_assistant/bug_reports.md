# Structured Bug Reports — Prompting Debug Assistant

**Project:** Holberton AI for Developers — Prompting Debug Assistant  
**AI assistant:** ChatGPT (GPT-6)  
**Source:** `bug_snippets/` (original code)  
**Corrected code:** `bug_fixes/`  
**Validation evidence:** `bug_fixes/fix_validation.md` and `ai_debug_log.md`

## Bug Report – bug1.py
- **File Name**: `bug1.py` → `bug1_fixed.py`
- **Bug Summary**: A syntax error prevents the positive-integer sum program from running.
- **Root Cause**: The conditional statement `if number > 0` is missing its required trailing colon (`:`). Python raises `SyntaxError` before executing the function.
- **Resolution (AI Suggestion)**: Replace `if number > 0` with `if number > 0:`; preserve the existing indentation and calculation.
- **Manual Edits**: None beyond applying the AI-suggested one-character fix.
- **Validation**: Input `"3, -2, 5, 0"` → expected `Positive sum: 8`; actual `Positive sum: 8` (**PASS**). Additional tests for empty input and negative values passed.
- **Lessons Learned**: Syntax errors must be fixed before runtime debugging. Start with the reported line and make the smallest possible change.

## Bug Report – bug2.py
- **File Name**: `bug2.py` → `bug2_fixed.py`
- **Bug Summary**: A discount calculator increases prices instead of decreasing them.
- **Root Cause**: `price * (1 + discount_rate)` calculates a markup; the intended formula for a discount is `price * (1 - discount_rate)`.
- **Resolution (AI Suggestion)**: Replace `adjusted = price * (1 + discount_rate)` with `adjusted = price * (1 - discount_rate)`.
- **Manual Edits**: None beyond applying the AI-suggested correction.
- **Validation**: Input `[100.0, 50.0, 30.0]`, rate `0.10` → expected `[90.0, 45.0, 27.0]`; actual `[90.0, 45.0, 27.0]` (**PASS**). Zero and 100% discount checks passed.
- **Lessons Learned**: Code that runs without exceptions can still be wrong. Validate business logic with concrete expected values and boundary cases.

## Bug Report – bug3.js
- **File Name**: `bug3.js` → `bug3_fixed.js`
- **Bug Summary**: Filtering passing users crashes with a JavaScript `TypeError`.
- **Root Cause**: The code reads `user.profile.score`, but input objects store `score` directly and contain no `profile` object. Reading a property from `undefined` throws an exception.
- **Resolution (AI Suggestion)**: Replace `user.profile.score` with `user.score`, matching the actual input schema.
- **Manual Edits**: None beyond applying the AI-suggested property-access correction.
- **Validation**: Threshold `70` with Ada (84), Lin (72), and Sam (48) → expected `['Ada', 'Lin']`; actual `['Ada', 'Lin']` (**PASS**). Empty and all-failing user arrays passed.
- **Lessons Learned**: Confirm the shape of input data before accessing nested properties. A stack trace identifies the failure location, but the data contract explains the cause.

## Bug Report – bug4.js
- **File Name**: `bug4.js` → `bug4_fixed.js`
- **Bug Summary**: Returning the last `n` array items omits one required element.
- **Root Cause**: `items.length - count + 1` begins one index too late, producing an off-by-one error.
- **Resolution (AI Suggestion)**: Replace `const start = items.length - count + 1;` with `const start = items.length - count;`.
- **Manual Edits**: None beyond applying the AI-suggested index correction. Validation remained within the function's stated valid count range.
- **Validation**: Input `[10, 20, 30, 40, 50]`, count `3` → expected `[30, 40, 50]`; actual `[30, 40, 50]` (**PASS**). Count `0` and count equal to array length also passed.
- **Lessons Learned**: Array indexing is zero-based. Test boundary counts (`0`, `1`, full length), not just a typical case.

## Bug Report – bug5.cpp
- **File Name**: `bug5.cpp` → `bug5_fixed.cpp`
- **Bug Summary**: Computing an average returns `4` instead of the expected fractional value `4.33333`.
- **Root Cause**: `total / scores.size()` performs integral division before conversion to the function's `double` return type, discarding the fractional part.
- **Resolution (AI Suggestion)**: Replace `return total / scores.size();` with `return static_cast<double>(total) / scores.size();` to ensure floating-point division.
- **Manual Edits**: None beyond applying the AI-suggested explicit cast. The original assumption of a nonempty vector remains unchanged.
- **Validation**: Input `{4, 4, 5}` → expected `Average: 4.33333`; actual `Average: 4.33333` (**PASS**). Additional input `{1, 2}` produced `1.5`.
- **Lessons Learned**: The arithmetic operation's operand types determine its behavior; assigning a truncated result to a floating-point variable cannot recover lost precision.

## Overall Debugging Summary

| Original File | Category | AI-Suggested Fix | Manual Adjustments | Validation |
|---|---|---|---|---|
| `bug1.py` | Syntax | Add missing `:` | None | PASS |
| `bug2.py` | Logic | Use `1 - discount_rate` | None | PASS |
| `bug3.js` | Runtime | Read `user.score` | None | PASS |
| `bug4.js` | Off-by-one | Remove extra `+1` | None | PASS |
| `bug5.cpp` | Types | Cast numerator to `double` | None | PASS |

**Conclusion:** ChatGPT proposed minimal corrections. Each proposed fix was applied to a separate corrected file and validated by executing the program and checking expected versus actual output. The original buggy snippets were retained for reproducibility. No additional manual code changes beyond the AI suggestions were required.
