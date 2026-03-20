result1 = df.groupby('Date').apply(lambda x: x.eq(0).sum())
result2 = df.groupby('Date').apply(lambda x: x.ne(0).sum())

print(result1)
print(result2)
