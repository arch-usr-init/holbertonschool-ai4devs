# Bug Descriptions

## Bug 1 – bug1.py
**Intended Behavior**: Read comma-separated integers, ignore non-positive values, and return the sum of positive integers. Input "3, -2, 5, 0" should produce 8.

**Issue Type**: Syntax error.

**Notes**: The conditional statement `if number > 0` is missing a colon. Python raises SyntaxError before execution.

## Bug 2 – bug2.py
**Intended Behavior**: Apply a percentage discount to product prices. A 10% discount on [100.0, 50.0, 30.0] should return [90.0, 45.0, 27.0].

**Issue Type**: Logical error.

**Notes**: The formula multiplies by (1 + discount_rate) instead of (1 - discount_rate), increasing prices rather than reducing them.

## Bug 3 – bug3.js
**Intended Behavior**: Select users whose scores meet or exceed a minimum threshold. For a threshold of 70, return ["Ada", "Lin"].

**Issue Type**: Runtime exception.

**Notes**: The program accesses `user.profile.score`, but the input objects store `score` directly. Accessing `score` through an undefined profile produces a TypeError.

## Bug 4 – bug4.js
**Intended Behavior**: Return the last requested number of elements from an array. For [10, 20, 30, 40, 50] and count 3, return [30, 40, 50].

**Issue Type**: Off-by-one error / loop logic issue.

**Notes**: The starting index uses `items.length - count + 1`, skipping the first required element. The extra +1 causes the incorrect result.

## Bug 5 – bug5.cpp
**Intended Behavior**: Calculate the floating-point arithmetic mean of integer scores. For [4, 4, 5], return approximately 4.33333.

**Issue Type**: Misuse of data types / integer division.

**Notes**: The division is performed using integer operands, causing truncation before conversion to double. Floating-point division is needed.
