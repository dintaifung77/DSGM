import pandas as pd
from statsmodels.multivariate.factor import Factor

df = pd.read_csv('gogoro_data.csv')
sat_items = df[['Sat1', 'Sat2']]

fa = Factor(sat_items.values, n_factor=1, method='pa')
result = fa.fit()

print("Loadings for Satisfaction Items:")
print(result.loadings.flatten())