# Tested Prompt Examples

This document demonstrates five prompt engineering patterns. Each example includes the prompt used, input provided, AI output, and feedback evaluating the result.

---

## Example 1: Role-Based Prompting

### Prompt Used
Act as an experienced software developer. Explain what a variable is in Python to a beginner. Use a simple real-life example and a short Python code example.

### Input Provided
Explain Python variables to someone who has never programmed before.

### Actual AI Output
A variable is like a labeled box where you can store information.

For example:

```python
name = "Alex"
age = 20
```

Here, `name` stores the text "Alex", while `age` stores the number 20. You can use these variables later in your program.

### Feedback
The output is clear, beginner-friendly, and uses a relatable analogy. The code example reinforces the explanation. Role-based prompting helps establish the expertise and communication style expected from the AI.

---

## Example 2: Few-Shot Prompting

### Prompt Used
Convert informal sentences into professional language.

Examples:

Input: "I need help with this task."
Output: "I would appreciate your assistance with this task."

Input: "I can't attend the meeting."
Output: "Unfortunately, I will be unable to attend the meeting."

Now convert this sentence:

"I don't understand the instructions."

### Input Provided
"I don't understand the instructions."

### Actual AI Output
"I would appreciate further clarification regarding the instructions."

### Feedback
The AI followed the demonstrated pattern and produced a professional alternative. Providing examples before the actual request helped establish the expected transformation style.

---

## Example 3: Step-by-Step Prompting

### Prompt Used
Solve the following problem step by step. Explain your reasoning clearly and provide the final answer separately.

A store sells a laptop for $800 and offers a 10% discount. Calculate the discounted price.

### Input Provided
Original price: $800  
Discount: 10%

### Actual AI Output
Step 1: Calculate the discount amount.

10% of $800 = 800 × 0.10 = $80.

Step 2: Subtract the discount from the original price.

$800 - $80 = $720.

Final Answer: The discounted laptop price is $720.

### Feedback
The output breaks the calculation into understandable steps and provides the correct result. The structured instruction makes the response easier to follow and verify.

---

## Example 4: Output Format Prompting

### Prompt Used
Explain three benefits of regular exercise.

Return the answer in a Markdown table with exactly three columns: Benefit, Explanation, and Example.

### Input Provided
Topic: Benefits of regular exercise.

### Actual AI Output
| Benefit | Explanation | Example |
|---|---|---|
| Better physical health | Exercise supports cardiovascular health and muscle strength. | Walking or cycling. |
| Improved mental well-being | Physical activity can help reduce stress and improve mood. | Running or yoga. |
| Increased energy | Regular activity can improve stamina over time. | Daily brisk walking. |

### Feedback
The AI followed the requested Markdown table structure and provided three relevant benefits. Explicit output formatting makes the response easier to read and organize.

---

## Example 5: Constraint-Based Prompting

### Prompt Used
Write a short explanation of cybersecurity.

Requirements:
- Use simple English.
- Maximum 50 words.
- Avoid technical jargon.
- Include one practical example.

### Input Provided
Topic: Cybersecurity.

### Actual AI Output
Cybersecurity means protecting computers, phones, and personal information from online threats. For example, using a strong password and two-factor authentication can help prevent unauthorized people from accessing your accounts.

### Feedback
The response follows the requested simplicity and length constraints while including a practical example. Clearly defined constraints help control the length, complexity, and relevance of AI-generated content.

---

## Conclusion

These five examples demonstrate different prompt engineering techniques:

1. Role-Based Prompting establishes the AI's role and expertise.
2. Few-Shot Prompting demonstrates the desired response through examples.
3. Step-by-Step Prompting encourages structured problem-solving.
4. Output Format Prompting controls how information is presented.
5. Constraint-Based Prompting limits and guides the response.

Each technique helps improve communication with AI systems by making instructions more specific, structured, and understandable.# Tested Prompt Examples

# Tested Prompt Examples

This document demonstrates five prompt engineering patterns. Each example includes the prompt used, input provided, AI output, and feedback evaluating the result.

---

## Example 1: Role-Based Prompting

### Prompt Used
Act as an experienced software developer. Explain what a variable is in Python to a beginner. Use a simple real-life example and a short Python code example.

### Input Provided
Explain Python variables to someone who has never programmed before.

### Actual AI Output
A variable is like a labeled box where you can store information.

For example:

```python
name = "Alex"
age = 20
```

Here, `name` stores the text "Alex", while `age` stores the number 20. You can use these variables later in your program.

### Feedback
The output is clear, beginner-friendly, and uses a relatable analogy. The code example reinforces the explanation. Role-based prompting helps establish the expertise and communication style expected from the AI.

---

## Example 2: Few-Shot Prompting

### Prompt Used
Convert informal sentences into professional language.

Examples:

Input: "I need help with this task."
Output: "I would appreciate your assistance with this task."

Input: "I can't attend the meeting."
Output: "Unfortunately, I will be unable to attend the meeting."

Now convert this sentence:

"I don't understand the instructions."

### Input Provided
"I don't understand the instructions."

### Actual AI Output
"I would appreciate further clarification regarding the instructions."

### Feedback
The AI followed the demonstrated pattern and produced a professional alternative. Providing examples before the actual request helped establish the expected transformation style.

---

## Example 3: Step-by-Step Prompting

### Prompt Used
Solve the following problem step by step. Explain your reasoning clearly and provide the final answer separately.

A store sells a laptop for $800 and offers a 10% discount. Calculate the discounted price.

### Input Provided
Original price: $800  
Discount: 10%

### Actual AI Output
Step 1: Calculate the discount amount.

10% of $800 = 800 × 0.10 = $80.

Step 2: Subtract the discount from the original price.

$800 - $80 = $720.

Final Answer: The discounted laptop price is $720.

### Feedback
The output breaks the calculation into understandable steps and provides the correct result. The structured instruction makes the response easier to follow and verify.

---

## Example 4: Output Format Prompting

### Prompt Used
Explain three benefits of regular exercise.

Return the answer in a Markdown table with exactly three columns: Benefit, Explanation, and Example.

### Input Provided
Topic: Benefits of regular exercise.

### Actual AI Output
| Benefit | Explanation | Example |
|---|---|---|
| Better physical health | Exercise supports cardiovascular health and muscle strength. | Walking or cycling. |
| Improved mental well-being | Physical activity can help reduce stress and improve mood. | Running or yoga. |
| Increased energy | Regular activity can improve stamina over time. | Daily brisk walking. |

### Feedback
The AI followed the requested Markdown table structure and provided three relevant benefits. Explicit output formatting makes the response easier to read and organize.

---

## Example 5: Constraint-Based Prompting

### Prompt Used
Write a short explanation of cybersecurity.

Requirements:
- Use simple English.
- Maximum 50 words.
- Avoid technical jargon.
- Include one practical example.

### Input Provided
Topic: Cybersecurity.

### Actual AI Output
Cybersecurity means protecting computers, phones, and personal information from online threats. For example, using a strong password and two-factor authentication can help prevent unauthorized people from accessing your accounts.

### Feedback
The response follows the requested simplicity and length constraints while including a practical example. Clearly defined constraints help control the length, complexity, and relevance of AI-generated content.

---

## Conclusion

These five examples demonstrate different prompt engineering techniques:

1. Role-Based Prompting establishes the AI's role and expertise.
2. Few-Shot Prompting demonstrates the desired response through examples.
3. Step-by-Step Prompting encourages structured problem-solving.
4. Output Format Prompting controls how information is presented.
5. Constraint-Based Prompting limits and guides the response.

Each technique helps improve communication with AI systems by making instructions more specific, structured, and understandable.
