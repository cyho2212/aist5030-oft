df['A'] = df['A'].str.replace('&AMP;', '&')
df['C'] = df['C'].str.replace('&AMP;', '&')

print(df)
