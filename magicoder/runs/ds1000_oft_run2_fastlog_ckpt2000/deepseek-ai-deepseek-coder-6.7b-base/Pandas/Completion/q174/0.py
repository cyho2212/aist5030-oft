df = pd.DataFrame(s.sort_values(ascending=False).reset_index())
df.columns = ['index', '1']
print(df)
