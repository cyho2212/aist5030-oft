result = pd.merge(df_a, df_b, on='EntityNum')
result = result.drop('b_col', axis=1)

print(result)
