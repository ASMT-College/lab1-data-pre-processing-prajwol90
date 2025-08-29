import pandas as pd

print("Prajwol lab 1.1")
# Load data
df = pd.read_csv('employee_data.csv')

# Fill missing values with mean, convert to int
df['Age'] = df['Age'].fillna(df['Age'].mean()).astype(int)
df['Salary'] = df['Salary'].fillna(df['Salary'].mean()).astype(int)

# Standardize department names
df['Department'] = df['Department'].replace({'Human Resources': 'HR', 'H.R.': 'HR', 'hr': 'HR'})

# Remove duplicates by ID
df = df.drop_duplicates(subset='ID')

# Show and save cleaned data
print("Cleaned Data:\n", df)
df.to_csv('cleaned_employee.csv', index=False)
