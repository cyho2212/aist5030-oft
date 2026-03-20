df[['fips', 'medi', 'row']] = df['row'].str.split(' ', expand=True)
print(df)
