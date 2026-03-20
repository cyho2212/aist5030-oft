result = pd.pivot_table(df, values=['D','E'], index=['B'], aggfunc={'D': np.max, 'E': np.min})
print(result)
