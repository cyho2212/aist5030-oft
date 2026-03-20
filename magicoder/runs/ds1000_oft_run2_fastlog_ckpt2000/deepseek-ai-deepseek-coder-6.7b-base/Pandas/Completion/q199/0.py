df['fips'] = df['row'].str[:5]
df['row'] = df['row'].str[6:]

print(df)
