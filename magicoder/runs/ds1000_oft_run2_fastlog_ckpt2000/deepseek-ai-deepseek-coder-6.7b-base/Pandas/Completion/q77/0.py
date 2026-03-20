result = df.groupby(df.index // 3).sum()

print(result)
