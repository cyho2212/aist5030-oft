result = df.loc[0].ne(df.loc[8]).index[df.loc[0].ne(df.loc[8])].tolist()
print(result)
