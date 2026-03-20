result = df.loc[0].where(df.loc[0] == df.loc[8]).dropna().index
print(result)
