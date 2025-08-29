import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
print("Prajwol Lab-1.5")
md = pd.read_csv('medical_data.csv')
print("Initial Data: \n", md.head())
X = md.drop(columns=['Disease'])
y = md['Disease']
selector = SelectKBest(score_func=chi2, k=3)
selector.fit(X, y)
top_features = X.columns[selector.get_support()]
print("\nTop 3 Features for Predicting Disease:\n", top_features)