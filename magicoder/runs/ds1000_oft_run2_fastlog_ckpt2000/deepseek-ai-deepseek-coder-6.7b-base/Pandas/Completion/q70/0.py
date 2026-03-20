    locs = [df.columns.get_loc(_) for _ in columns]
    return df[df.c > 0.5][locs].values

# Test
df = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
print(f(df))
