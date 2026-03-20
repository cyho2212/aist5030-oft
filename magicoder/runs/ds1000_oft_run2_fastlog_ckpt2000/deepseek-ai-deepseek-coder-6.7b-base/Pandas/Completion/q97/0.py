df = df.loc[df.abs().lt(1).all(axis=1)]
print(df)
