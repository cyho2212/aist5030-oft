df['fips'] = df['row'].str[:3]
df['row'] = df['row'].str[4:]

print(df)
