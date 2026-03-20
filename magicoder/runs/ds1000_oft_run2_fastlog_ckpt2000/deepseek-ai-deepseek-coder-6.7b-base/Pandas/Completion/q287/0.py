result = df.groupby(["id1","id2"])["foo","bar"].mean()
print(result)
