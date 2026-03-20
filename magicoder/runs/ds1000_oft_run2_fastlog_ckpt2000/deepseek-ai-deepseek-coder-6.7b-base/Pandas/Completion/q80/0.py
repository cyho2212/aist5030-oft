result = pd.concat([df.groupby(df.index // 3).sum(), df.groupby(df.index // 3).mean()], axis=1)

print(result)
