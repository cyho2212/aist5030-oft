result = df.groupby(['username', pd.cut(df['views'], bins)])['views'].count().unstack(fill_value=0)
print(result)
