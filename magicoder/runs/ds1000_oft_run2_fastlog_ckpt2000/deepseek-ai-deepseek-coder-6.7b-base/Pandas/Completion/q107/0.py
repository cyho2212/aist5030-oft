def validate_single_space_name(name: str) -> str:
    pattern = re.compile(r'^.*( ){1}.*$')
    match_obj = re.match(pattern, name)
    if match_obj:
        return name
    else:
        return None

df['name'] = df['name'].apply(validate_single_space_name)
df = df[df['name'].notnull()]
df[['first_name', 'last_name']] = df['name'].str.split(' ', 1, expand=True)
df['middle_name'] = df['name'].str.split(' ', 1, expand=True)[1]
df = df.drop('name', axis=1)
print(df)
