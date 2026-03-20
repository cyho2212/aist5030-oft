def tau1(x):
    y = np.array(df['A']) #  keep one column fix and run it in the other two
    tau, p_value = stats.kendalltau(x, y)
    return tau

df['AB'] = df['B'].rolling(3).apply(tau1)
df['AC'] = df['C'].rolling(3).apply(tau1)
df['BC'] = df['B'].rolling(3).apply(tau1)

print(df)
