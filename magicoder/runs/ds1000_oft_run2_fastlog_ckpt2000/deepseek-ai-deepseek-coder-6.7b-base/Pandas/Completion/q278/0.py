result = df[(df.index < '2020-02-17 15:30:00') | (df.index > '2020-02-18 21:59:00')]
print(result)
