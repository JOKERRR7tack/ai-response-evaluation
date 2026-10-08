# AI Response Evaluation & Quality Assessment

A human-evaluation project assessing AI-generated responses across research, reasoning, writing, data, and information-literacy tasks.

## What this demonstrates
- Designing a repeatable AI evaluation rubric
- Human assessment of model outputs
- Structured CSV data collection
- Error classification
- Python/pandas analysis
- Basic data visualization
- Reproducible Git/GitHub documentation

## Dataset
15 mixed-task evaluation cases. Each response is scored 1–5 for Accuracy, Relevance, Completeness, Clarity, and Instruction Following, plus factual-error status, error type, confidence, and a short evaluator rationale.

## Analysis
Run `python src/analyze_evaluations.py` to calculate criterion averages, task-type averages, factual-error rate, and error-type counts and generate charts in `results/`.

## Important methodology note
This is a portfolio-scale human evaluation, not a controlled benchmark. Future improvements could include more cases, multiple evaluators, blinded outputs, inter-rater agreement, and comparisons across multiple AI systems.

## Tech
Python, pandas, Matplotlib, CSV, Jupyter Notebook, Git/GitHub.
