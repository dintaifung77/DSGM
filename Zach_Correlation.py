import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gogoro_data.csv')

df['Brand'] = df[['Brand1', 'Brand2']].mean(axis=1)
df['Func']  = df[['Func1',  'Func2' ]].mean(axis=1)
df['Usab']  = df[['Usab1',  'Usab2' ]].mean(axis=1)
df['Price'] = df[['Price1', 'Price2']].mean(axis=1)
df['Sat']   = df[['Sat1',   'Sat2'  ]].mean(axis=1)
df['Loyal'] = df[['Loyal1', 'Loyal2']].mean(axis=1)

constructs = df[['Brand', 'Func', 'Usab', 'Price', 'Sat', 'Loyal']]
corr_matrix = constructs.corr().round(3)
print(corr_matrix)