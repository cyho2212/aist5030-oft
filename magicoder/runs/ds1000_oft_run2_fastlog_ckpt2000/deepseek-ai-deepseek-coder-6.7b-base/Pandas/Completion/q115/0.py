df['total'] = df.sum(axis=1)
df = df.div(df['total'], axis=0)
df = df.drop('total', axis=1)
print(df)
