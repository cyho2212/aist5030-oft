    df.index = pd.to_datetime(df.index)
    df = df.swaplevel(0, 1, axis=0)
    return df

# Test
df = pd.DataFrame({'x': [100, 90, 80], 'y': [7, 8, 9]}, index=pd.MultiIndex.from_tuples([('3/1/1994', 'abc'), ('9/1/1994', 'abc'), ('3/1/1995', 'abc')]))
print(f(df))
