result = df.groupby('r')['v'].apply(lambda x: x.sum(skipna=False))
print(result)
