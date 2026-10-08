import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/evaluation_dataset.csv")

score_cols = ["accuracy", "relevance", "completeness", "clarity", "instruction_following"]
df["overall_score"] = df[score_cols].mean(axis=1)

print("Overall average:", round(df["overall_score"].mean(), 2))
print("\nAverage by task type:")
print(df.groupby("task_type")["overall_score"].mean().round(2))

print("\nAverage by criterion:")
print(df[score_cols].mean().round(2))

print("\nFactual error rate:")
print(round((df["factual_error"].eq("Yes").mean()) * 100, 2), "%")

summary = df.groupby("task_type")["overall_score"].mean().sort_values()
summary.plot(kind="bar", title="Average AI Response Score by Task Type",
             ylabel="Average Score (1-5)", xlabel="Task Type")
plt.tight_layout()
plt.savefig("results/average_score_by_task_type.png", dpi=150)
plt.show()
