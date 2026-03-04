import pandas as pd

df = pd.read_csv('gogoro_data.csv')
v_df = df.copy()

# Drop missing values
v_df = v_df.dropna()

# Check for straight-lining: variance across a subset of items
survey_cols = ['Func1', 'Func2', 'Usab1', 'Usab2']
v_df['Variance'] = v_df[survey_cols].var(axis=1)

v_df = v_df[v_df['Variance'] > 0]
print("Rows remaining:", len(v_df))