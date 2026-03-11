import pandas as pd
from scipy import stats

df = pd.read_csv('gogoro_data.csv')

# Assessing normality for the Brand1 item (Shapiro-Wilk)
stat, p = stats.shapiro(df['Brand1'])
norm_test = pd.DataFrame({'W': [round(stat, 4)], 'pval': [round(p, 4)]},
                         index=['Brand1'])
print(norm_test)