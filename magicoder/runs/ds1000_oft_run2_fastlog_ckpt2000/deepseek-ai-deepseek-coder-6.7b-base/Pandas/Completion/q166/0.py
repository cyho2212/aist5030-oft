result = df.groupby('a')['b'].agg(['mean', 'std'])
print(result)
