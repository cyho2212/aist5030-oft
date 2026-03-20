df = df.select_dtypes(include=['number'])
df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
