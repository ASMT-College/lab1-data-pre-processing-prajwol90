import pandas as pd
print("Prajwol lab-1.2")
from sklearn.preprocessing import MinMaxScaler
d = pd.read_csv('student_scores.csv')

print('Initial students score: \n', d.head())

scaler = MinMaxScaler()
d[['Math', 'Science', 'English']] = scaler.fit_transform(d[['Math', 'Science', 'English']])
print("\nNormalized Scores:\n", d.head())

print(d.columns)