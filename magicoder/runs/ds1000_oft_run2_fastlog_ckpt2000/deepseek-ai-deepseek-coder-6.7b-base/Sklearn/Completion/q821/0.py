df_out = pd.get_dummies(df.Col3.apply(pd.Series).stack()).sum(level=0)
df_out.index = df.index
df_out = df.join(df_out)
df_out = df_out.drop('Col3', axis=1)
