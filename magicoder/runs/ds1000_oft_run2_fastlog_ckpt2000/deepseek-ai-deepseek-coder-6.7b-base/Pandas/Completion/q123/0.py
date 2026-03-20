cols = [df.keywords_0, df.keywords_1, df.keywords_2, df.keywords_3]
df["keywords_all"] = df[cols].apply(lambda row: ", ".join(row.dropna().astype(str)), axis=1)

print(df)
