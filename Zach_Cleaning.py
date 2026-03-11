import pandas as pd

df = pd.read_csv('gogoro_data.csv')
v_df = df.copy()

# Report missing data before cleaning
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({'Missing Count': missing, 
                               'Missing %': missing_pct})
missing_report = missing_report[missing_report['Missing Count'] > 0]
if missing_report.empty:
    print("No missing values detected.")
else:
    print("Missing Data Report:")
    print(missing_report)
print(f"Total rows before cleaning: {len(v_df)}")

# Drop missing values
v_df = v_df.dropna()
print(f"Rows after dropping missing values: {len(v_df)}")

# Check for straight-lining: variance across a subset of items
survey_cols = ['Func1', 'Func2', 'Usab1', 'Usab2']
v_df['Variance'] = v_df[survey_cols].var(axis=1)
n_straightline = (v_df['Variance'] <= 0).sum()
print(f"Straight-lining cases detected: {n_straightline}")

v_df = v_df[v_df['Variance'] > 0]
print(f"Rows remaining after cleaning: {len(v_df)}")