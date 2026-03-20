df['2001'] = df['2001'].cumsum() / (df['2001'] != 0).cumsum()
df['2002'] = df['2002'].cumsum() / (df['2002'] != 0).cumsum()
df['2003'] = df['2003'].cumsum() / (df['2003'] != 0).cumsum()
df['2004'] = df['2004'].cumsum() / (df['2004'] != 0).cumsum()
df['2005'] = df['2005'].cumsum() / (df['2005'] != 0).cumsum()
df['2006'] = df['2006'].cumsum() / (df['2006'] != 0).cumsum()

print(df)
