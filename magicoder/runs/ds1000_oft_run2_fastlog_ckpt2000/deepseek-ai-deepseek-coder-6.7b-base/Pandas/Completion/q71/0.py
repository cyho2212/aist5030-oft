    df = df[df.c > 0.5][columns]
    df['sum'] = df.sum(axis=1)
    return df

# Test
df = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
print(f(df))
