from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/evaluation_dataset.csv')
criteria=['accuracy','relevance','completeness','clarity','instruction_following']
df['overall_score']=df[criteria].mean(axis=1)
print('Overall:',round(df.overall_score.mean(),2))
print('\nCriteria:\n',df[criteria].mean().round(2))
print('\nTasks:\n',df.groupby('task_type').overall_score.mean().round(2))
print('\nFactual-error rate:',round((df.factual_error=='Yes').mean()*100,1),'%')
r=ROOT/'results'; r.mkdir(exist_ok=True)
df[criteria].mean().sort_values().plot(kind='barh',xlim=(0,5),title='Average Score by Criterion')
plt.xlabel('Average score (1–5)'); plt.tight_layout(); plt.savefig(r/'criterion_averages.png',dpi=160); plt.close()
df.groupby('task_type').overall_score.mean().sort_values().plot(kind='barh',xlim=(0,5),title='Average AI Response Quality by Task Type')
plt.xlabel('Average score (1–5)'); plt.tight_layout(); plt.savefig(r/'task_comparison.png',dpi=160); plt.close()
df[df.error_type!='None'].error_type.value_counts().plot(kind='bar',title='Observed Error Types')
plt.ylabel('Number of cases'); plt.tight_layout(); plt.savefig(r/'error_types.png',dpi=160); plt.close()
