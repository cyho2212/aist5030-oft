result = pd.DataFrame({'user': df['user'].unique(), 'dt': pd.date_range(df['dt'].min(), df['dt'].max())})
result = result.merge(df, on=['user', 'dt'], how='left').fillna(0)
print(result)
