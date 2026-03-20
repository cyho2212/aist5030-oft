result = df.apply(pd.Series.value_counts).fillna(0).stack().astype(int)
print(result)
