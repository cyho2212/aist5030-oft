df = df.set_index('cat')
df = df.div(df.sum(axis=1), axis=0)
df = df.reset_index()
print(df)
