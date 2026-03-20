    for col in df.columns:
        df[col] = df[col].str.replace('&AMP;', '&')
    return df

print(f())
