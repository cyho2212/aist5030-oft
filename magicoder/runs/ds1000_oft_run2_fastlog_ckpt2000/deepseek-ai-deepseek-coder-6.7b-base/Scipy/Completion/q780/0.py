result = pd.DataFrame(index=df.index)
for col in df.columns:
    result[col] = df[col].apply(lambda x: 'data {:.3f}'.format(x))
    result[col + '_zscore'] = df[col].apply(lambda x: 'zscore {:.3f}'.format(stats.zscore(x)))

print(result)
