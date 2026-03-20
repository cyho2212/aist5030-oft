df_out = pd.get_dummies(df.iloc[:, -1].apply(pd.Series).stack()).sum(level=0)
df_out.index = df.index
df_out = df.drop(df.columns[-1], axis=1).join(df_out)
