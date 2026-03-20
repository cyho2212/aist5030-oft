result = df.groupby(["id1","id2"])["foo","bar"].mean()
result = result.fillna(0)
print(result)
