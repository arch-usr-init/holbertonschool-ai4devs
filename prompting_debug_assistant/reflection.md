# Reflection on AI-Assisted Debugging

## Introduction

In this project, I used ChatGPT to diagnose five deliberately flawed programs written in Python, JavaScript, and C++. The cases included a syntax error, an incorrect discount calculation, a runtime exception, an off-by-one error, and integer division. For each case, I supplied the code and its intended behavior, considered the proposed correction, and checked the result using Python, Node.js, or a C++ compiler. This process helped me distinguish a plausible explanation from a verified repair.

## AI Strengths

The easiest case was `bug1.py`: a missing colon after `if number > 0` produced a Python `SyntaxError`. The AI diagnosis stated, "The condition `if number > 0` is missing the mandatory colon." This was precise, actionable, and easy to verify. The JavaScript off-by-one error in `bug4.js` was similarly straightforward: removing the extra `+ 1` restored the requested three elements. AI also identified that `bug2.py` increased prices because its formula used `1 + discount_rate` instead of subtraction. These responses accelerated initial triage by pointing directly to the relevant expressions without proposing unnecessary rewrites.

## AI Weaknesses

The more difficult cases required attention beyond whether the program executed successfully. In `bug5.cpp`, the average function compiled and returned a number, but integer division silently discarded the fractional part. Understanding the conversion rules mattered more than spotting an exception. In `bug3.js`, the runtime `TypeError` was obvious, but the correct fix depended on the actual user-object schema: the data contained `score`, not `profile.score`. AI supplied useful minimal fixes, yet none of those suggestions alone established robustness for arbitrary inputs. For example, the revised array-slicing logic was validated for a normal count, not for negative counts or counts larger than the array. No incorrect primary fix was observed in these five tests; the main limitation was incomplete assurance about untested edge cases.

## Human Role

I treated AI output as a hypothesis, not as authority. Human judgment defined the expected behavior, selected the smallest safe change, and determined meaningful assertions. I compared actual output against expected values: discounted prices became `[90.0, 45.0, 27.0]`, passing users became `Ada` and `Lin`, and the C++ average became approximately `4.33333`. I also kept the original buggy snippets separate from corrected versions so that the debugging evidence remained reproducible. This manual validation was essential because a clean exit status cannot prove that business logic is correct.

## Conclusion

Overall, AI made diagnosis faster for localized faults, especially syntax and indexing mistakes. It was most valuable as a debugging partner that explained causes and suggested small patches. Its limits became apparent when correctness depended on domain expectations, language semantics, or edge-case coverage. In professional development, I would combine AI-assisted analysis with tests, code review, version control, and regression checks. The effective workflow is to reproduce, diagnose, patch, execute, compare, and document, while keeping responsibility for correctness with the developer.
