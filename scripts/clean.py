import pandas as pd

df = pd.read_csv('disponibilidad_raw.csv', index_col=0, sep=';')
df = df.loc[:,df.columns[[5, 6, 7, 8, 9]]]
cols = list(df.columns)
new_cols = [c.split(':')[0] for c in cols]
df = df.rename(columns=dict(zip(cols, new_cols)))
df = df.dropna(how='all', axis=0)
df.to_csv('disponibilidad.csv')
