df = df.shift(1, axis=0)
df.iloc[-1] = df.iloc[0]
df = df.shift(-1, axis=0)
df.iloc[0] = df.iloc[-1]
print(df)
