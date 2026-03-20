df = df.shift(1, axis=0)
df.iloc[-1] = df.iloc[0]
df = df.drop(df.index[0])
print(df)
