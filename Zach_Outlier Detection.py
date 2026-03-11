import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gogoro_data.csv')

fig, axes = plt.subplots(1, 3, figsize=(10, 5))
for ax, col in zip(axes, ['Func1', 'Price1', 'Brand1']):
    ax.boxplot(df[col].dropna(), patch_artist=True,
               boxprops=dict(facecolor='steelblue', alpha=0.6))
    ax.set_title(col)
    ax.set_ylabel('Score')

    q1, q3 = df[col].quantile(0.25), df[col].quantile(0.75)
    iqr = q3 - q1
    n_out = ((df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)).sum()
    ax.set_xlabel(f'Outliers: {n_out}')

plt.suptitle('Univariate Outlier Detection via Boxplot')
plt.tight_layout()
plt.show()