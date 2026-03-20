df = df.shift(1)
df.iloc[0, 0] = df.iloc[-1, 0]
df.iloc[-1, 0] = df.iloc[0, 0]
df = df.shift(-1)
df.iloc[0, 0] = df.iloc[-1, 0]
df.iloc[-1, 0] = df.iloc[0, 0]

print(df)
