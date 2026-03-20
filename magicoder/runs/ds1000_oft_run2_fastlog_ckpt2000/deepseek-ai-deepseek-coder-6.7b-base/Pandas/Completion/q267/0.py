result = [(df.iloc[0][i], df.iloc[8][i]) for i in df.columns if df.iloc[0][i] != df.iloc[8][i]]
print(result)
