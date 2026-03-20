result = df.groupby(df.index // 4).sum()

print(result)
