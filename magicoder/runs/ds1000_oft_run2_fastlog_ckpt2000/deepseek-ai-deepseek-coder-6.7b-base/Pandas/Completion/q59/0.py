result = pd.DataFrame({'dt': pd.date_range(df['dt'].min(), df['dt'].max()), 'user': df['user'].unique()[0], 'val': df['val'].max()})
print(result)
