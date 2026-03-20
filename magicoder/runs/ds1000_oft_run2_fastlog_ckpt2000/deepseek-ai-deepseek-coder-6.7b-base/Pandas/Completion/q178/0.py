result = df.loc[df.groupby(['Sp','Mt'])['count'].idxmax()]
print(result)
