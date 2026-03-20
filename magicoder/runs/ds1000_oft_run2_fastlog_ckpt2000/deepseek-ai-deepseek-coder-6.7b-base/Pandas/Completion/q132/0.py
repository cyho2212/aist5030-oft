    df['index_original'] = df.index
    df['index_original'] = df.groupby(['col1', 'col2'])['index_original'].transform('first')
    return df

print(f())
