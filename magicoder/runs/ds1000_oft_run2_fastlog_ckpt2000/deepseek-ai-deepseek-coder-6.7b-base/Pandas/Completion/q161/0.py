result = df.groupby('cokey').apply(lambda x: x.sort_values('A', ascending=False)).reset_index(drop=True)
print(result)
