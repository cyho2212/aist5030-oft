result = pd.DataFrame(index=df.index)
for col in df.columns:
    result[col] = df[col]
    result[col+'_zscore'] = stats.zscore(df[col])

print(result)
