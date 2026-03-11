import pandas as pd
import numpy as np

df = pd.read_csv('gogoro_data.csv')
brand_items = df[['Brand1', 'Brand2']]

n = brand_items.shape[1]
item_vars = brand_items.var(ddof=1)
total_var = brand_items.sum(axis=1).var(ddof=1)
alpha = (n / (n - 1)) * (1 - item_vars.sum() / total_var)
print("Cronbach's Alpha (Brand Image):", round(alpha, 3))

df = pd.read_csv('gogoro_data.csv')
brand_items = df[['Func1', 'Func2']]

n = brand_items.shape[1]
item_vars = brand_items.var(ddof=1)
total_var = brand_items.sum(axis=1).var(ddof=1)
alpha = (n / (n - 1)) * (1 - item_vars.sum() / total_var)
print("Cronbach's Alpha (Function):", round(alpha, 3))

df = pd.read_csv('gogoro_data.csv')
brand_items = df[['Usab1', 'Usab2']]

n = brand_items.shape[1]
item_vars = brand_items.var(ddof=1)
total_var = brand_items.sum(axis=1).var(ddof=1)
alpha = (n / (n - 1)) * (1 - item_vars.sum() / total_var)
print("Cronbach's Alpha (Usability):", round(alpha, 3))

