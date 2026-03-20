df['1_name'] = df['name'].apply(lambda x: x.split(' ')[0] if ' ' in x else x)
df['2_name'] = df['name'].apply(lambda x: x.split(' ')[1] if ' ' in x else '')

print(df)
