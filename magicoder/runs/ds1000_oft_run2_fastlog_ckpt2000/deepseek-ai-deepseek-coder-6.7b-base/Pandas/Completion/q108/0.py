result = pd.merge_asof(df2, df1, left_on='Timestamp', right_on='Timestamp', direction='backward')
print(result)
