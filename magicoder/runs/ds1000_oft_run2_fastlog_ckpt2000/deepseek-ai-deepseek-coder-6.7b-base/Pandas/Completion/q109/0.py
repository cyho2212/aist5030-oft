result = pd.merge_asof(df1, df2, left_on='Timestamp', right_on='Timestamp', direction='forward')

print(result)
