conditions = [df['a'].str.contains(target)]
result = np.select(conditions, choices, default=np.nan)
print(result)
