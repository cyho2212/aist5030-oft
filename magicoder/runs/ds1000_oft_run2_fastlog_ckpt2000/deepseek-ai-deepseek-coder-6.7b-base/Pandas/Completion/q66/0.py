df = df.melt(id_vars=['user'], var_name='others', value_name='value')

print(df)
