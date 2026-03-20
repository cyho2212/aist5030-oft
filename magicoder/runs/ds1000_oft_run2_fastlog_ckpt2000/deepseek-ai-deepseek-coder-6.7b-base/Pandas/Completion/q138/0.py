result = df.loc[df.groupby(['Sp','Value'])['count'].idxmax()]
print(result)
