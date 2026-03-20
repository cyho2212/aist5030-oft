result = pd.merge(df_a, df_b, on='EntityNum', how='left')
result = result.drop('a_col', axis=1)

print(result)
