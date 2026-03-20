    for col in df.columns:
        value_counts = df[col].value_counts()
        df[col] = df[col].apply(lambda x: 'other' if value_counts[x] < 2 else x)
    return df

print(f())
