    df['SOURCE_NAME'] = df['SOURCE_NAME'].str.split('_').str[0]
    return df

print(f())
