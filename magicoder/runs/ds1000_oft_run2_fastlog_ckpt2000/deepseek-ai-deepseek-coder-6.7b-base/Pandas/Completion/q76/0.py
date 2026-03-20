result = df.groupby(df.index // 3).mean()

print(result)
