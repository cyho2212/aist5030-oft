df['first_name'] = df['name'].apply(lambda x: x.split(' ')[0] if ' ' in x else x)
df['last_name'] = df['name'].apply(lambda x: x.split(' ')[1] if ' ' in x else None)

print(df)
