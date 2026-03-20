    df.index = pd.to_datetime(df.index)
    return df.values

# Test
df = pd.DataFrame({'x': [100, 90, 80], 'y': [7, 8, 9]}, index=['3/1/1994', '9/1/1994', '3/1/1995'])
print(f(df))
