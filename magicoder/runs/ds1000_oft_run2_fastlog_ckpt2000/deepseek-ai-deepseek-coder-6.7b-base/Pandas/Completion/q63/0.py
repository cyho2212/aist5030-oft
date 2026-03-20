    df['name'] = df['name'].astype('category').cat.codes
    return df

print(f())
