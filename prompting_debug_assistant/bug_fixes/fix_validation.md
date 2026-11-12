# Fix Validation — Prompting Debug Assistant, Task 2

**Scope:** Corrected versions of the five Task 0 snippets. The original buggy files in `../bug_snippets/` remain unchanged.  
**Environment:** Python 3, Node.js, and C++17 (`g++`).  
**Method:** Run each corrected program and compare actual output with expected output; perform additional valid-input assertions to check behavior. All cases below were executed successfully.

## Bug 1 – bug1_fixed.py
- **Input**: `"3, -2, 5, 0"`
- **Expected Output**: `Positive sum: 8`
- **Actual Output**: `Positive sum: 8` ✅
- **Additional tests**: `sum_positive("") == 0`; `sum_positive("-4,0,2,5") == 7` ✅
- **Command**: `python3 bug1_fixed.py`
- **Fix**: Added missing `:` to `if number > 0:`.
- **Manual tweaks beyond AI suggestion**: None.

## Bug 2 – bug2_fixed.py
- **Input**: `prices=[100.0,50.0,30.0]`, `discount_rate=0.10`
- **Expected Output**: `Sale prices: [90.0, 45.0, 27.0]`
- **Actual Output**: `Sale prices: [90.0, 45.0, 27.0]` ✅
- **Additional tests**: Zero discount preserves `[100,50]`; 100% discount yields `[0,0]` ✅
- **Command**: `python3 bug2_fixed.py`
- **Fix**: Replaced `(1 + discount_rate)` with `(1 - discount_rate)`.
- **Manual tweaks beyond AI suggestion**: None.

## Bug 3 – bug3_fixed.js
- **Input**: Users `[{name:"Ada",score:84},{name:"Lin",score:72},{name:"Sam",score:48}]`, threshold `70`
- **Expected Output**: `Passing users: [ 'Ada', 'Lin' ]`
- **Actual Output**: `Passing users: [ 'Ada', 'Lin' ]` ✅
- **Additional tests**: Empty users and all-failing users both return an empty array ✅
- **Command**: `node bug3_fixed.js`
- **Fix**: Replaced `user.profile.score` with `user.score`, matching the provided object schema.
- **Manual tweaks beyond AI suggestion**: None.

## Bug 4 – bug4_fixed.js
- **Input**: `items=[10,20,30,40,50]`, `count=3`
- **Expected Output**: `Last items: [ 30, 40, 50 ]`
- **Actual Output**: `Last items: [ 30, 40, 50 ]` ✅
- **Additional tests**: `count=0` returns `[]`; `count=items.length` returns the complete array ✅
- **Command**: `node bug4_fixed.js`
- **Fix**: Removed extra `+1` from start index (`items.length - count`).
- **Manual tweaks beyond AI suggestion**: None. Out-of-range counts are not handled by the original function and remain outside these tests.

## Bug 5 – bug5_fixed.cpp
- **Input**: `scores={4,4,5}`
- **Expected Output**: `Average: 4.33333`
- **Actual Output**: `Average: 4.33333` ✅
- **Additional test**: `scores={1,2}` prints `Average: 1.5` ✅
- **Commands**: `g++ -std=c++17 bug5_fixed.cpp -o bug5 && ./bug5`
- **Fix**: Converted numerator to `double` using `static_cast<double>(total)` before division.
- **Manual tweaks beyond AI suggestion**: None. Function assumes a non-empty vector, as in the original intended behavior.

## Summary

| File | Original problem | Corrected program | Extra tests | Verdict |
|---|---|---|---|---|
| `bug1_fixed.py` | Syntax error | Exit 0; sum 8 | 2 passed | PASS |
| `bug2_fixed.py` | Incorrect formula | Exit 0; discounted prices | 2 passed | PASS |
| `bug3_fixed.js` | TypeError | Exit 0; Ada and Lin | 2 passed | PASS |
| `bug4_fixed.js` | Off-by-one | Exit 0; final 3 items | 2 passed | PASS |
| `bug5_fixed.cpp` | Integer division | Compiled, exit 0; mean 4.33333 | 1 passed | PASS |

**Validation conclusion:** All five AI-suggested minimal fixes were applied, executed and validated against their intended examples. No additional manual code modifications were required.
