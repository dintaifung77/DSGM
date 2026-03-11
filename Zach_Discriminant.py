import pandas as pd

df = pd.read_csv('gogoro_data.csv')
df['Func_Score'] = df[['Func1', 'Func2']].mean(axis=1)
df['Usab_Score'] = df[['Usab1', 'Usab2']].mean(axis=1)

correlation = df['Func_Score'].corr(df['Usab_Score'])
print("Correlation (Function ~ Usability):", round(correlation, 3))