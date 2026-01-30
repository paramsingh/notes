
# LLM Temporal Reasoning Failures

Side project idea: Study when/why LLMs mess up dates and days, test interventions.

## Hook

"Your AI assistant probably can't tell you what day January 17th is. Here's why, and how to fix it."

## Prior Art

- **Test of Time (ToT)** - ICLR 2025. Off-by-one errors are most common (~21% of GPT-4 errors exactly 1 day off)
- **DATETIME benchmark** - Even trivial tasks show poor performance
- **TIME benchmark** - Real-world temporal reasoning

## Gap / Contribution

Existing work = benchmarks. Missing:
1. Day-of-week ↔ date mismatch specifically
2. Intervention testing (what actually fixes it?)
3. Practical recommendations for developers

## Research Questions

1. How often do models get day-of-week wrong for a given date?
2. Does the error rate change for near dates vs far dates?
3. Do planning tasks (multi-day, multi-week) compound errors?
4. Which interventions help?
   - Explicit date context
   - Chain-of-thought
   - Calendar tool access
   - Few-shot examples

## Test Categories

### Category 1: Simple Day-of-Week
- "What day of the week is January 17, 2026?"
- "What day of the week is March 3, 2026?"
- "What day of the week was December 25, 2025?"

### Category 2: Relative Date Calculation
- "If today is Saturday January 17, what date is next Wednesday?"
- "What's the date 10 days from January 17, 2026?"
- "If today is Thursday, and the date is January 15, what was last Monday's date?"

### Category 3: Day-Date Consistency (the Coach Vayu bug)
- "Create a workout plan for Monday, Wednesday, Friday starting January 20, 2026. Include the dates."
- "Schedule meetings for every Tuesday in February 2026. List all dates."
- "Plan a 4-week training program starting January 20. Show each day with its date."

### Category 4: Duration and Counting
- "How many days between January 17 and February 14, 2026?"
- "How many Mondays are in January 2026?"
- "If I run every other day starting January 17, list my next 10 run dates."

### Category 5: Edge Cases
- Month boundaries ("What day is February 1 if January 31 is a Friday?")
- Leap years ("Is 2024 a leap year? What day is February 29, 2024?")
- Year boundaries ("If December 31, 2025 is Wednesday, what day is January 1, 2026?")

## Interventions to Test

### A. Baseline
No date context. Just the question.

### B. Explicit Today Context
"Today is Saturday, January 17, 2026."

### C. Calendar Context
"Here is a calendar for January 2026:
Mon Tue Wed Thu Fri Sat Sun
         1   2   3   4   5
 6   7   8   9  10  11  12
13  14  15  16  17  18  19
20  21  22  23  24  25  26
27  28  29  30  31"

### D. Chain-of-Thought Prompt
"Think step by step. First verify what day of the week the starting date is, then proceed."

### E. Tool Access
Give the model a get_day_of_week(date) tool and see if it uses it correctly.

### F. Few-Shot Examples
Provide 2-3 correct examples before the test question.

## Models to Test

- Claude 3.5 Sonnet
- Claude 3 Opus
- GPT-4o
- GPT-4 Turbo
- Gemini 1.5 Pro
- Llama 3 70B
- Mistral Large

## Metrics

- **Accuracy**: % of correct day-of-week answers
- **Off-by-one rate**: % of errors that are exactly ±1 day
- **Consistency**: In planning tasks, do all day-date pairs match?
- **Intervention lift**: How much does each intervention improve accuracy?

## Methodology

1. Generate test set (aim for 100-200 questions across categories)
2. Run each question against each model with each intervention
3. Parse responses, extract day/date claims
4. Validate against ground truth (Python datetime)
5. Categorize errors
6. Statistical analysis of intervention effectiveness

## Output Format

Blog post or short paper:
1. Introduction (the problem, why it matters)
2. Related work (ToT, DATETIME, TIME)
3. Methodology
4. Results (tables, charts)
5. Analysis (why do models fail? which interventions work?)
6. Practical recommendations for developers
7. Limitations and future work

## Practical Recommendations (hypotheses)

Based on intuition, likely recommendations:
- Always include explicit "Today is [day], [date]" in system prompt
- For planning tasks, provide a calendar snippet
- Force CoT for multi-step date calculations
- Consider a simple date validation tool

## Timeline

Day 1:
- [ ] Generate test set
- [ ] Set up evaluation harness
- [ ] Run baseline tests across models

Day 2:
- [ ] Run intervention tests
- [ ] Analyze results
- [ ] Write up findings

## Why This Gets Attention

1. Practical problem every AI app developer faces
2. Actionable recommendations (not just "models are bad")
3. Builds on ICLR 2025 paper (ToT) with new angle
4. Clear, reproducible methodology
5. Good visuals potential (error heatmaps, intervention comparisons)

## Why This Gets You Hired

- Shows you understand LLM limitations deeply
- Demonstrates research methodology
- Practical engineering (building eval harness)
- Clear communication (blog post)
- Original contribution to the field
