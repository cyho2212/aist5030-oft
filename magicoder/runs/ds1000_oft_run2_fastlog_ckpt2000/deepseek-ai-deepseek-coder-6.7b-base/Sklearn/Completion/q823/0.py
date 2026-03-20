df_out = pd.get_dummies(df.Col4.apply(pd.Series).stack()).sum(level=0)
df_out = df.join(df_out)
df_out = df_out.drop('Col4', axis=1)
