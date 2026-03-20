result1 = df.groupby('Date').apply(lambda x: x.mod(2).eq(0).sum())
result2 = df.groupby('Date').apply(lambda x: x.mod(2).ne(0).sum())

print(result1)
print(result2)
