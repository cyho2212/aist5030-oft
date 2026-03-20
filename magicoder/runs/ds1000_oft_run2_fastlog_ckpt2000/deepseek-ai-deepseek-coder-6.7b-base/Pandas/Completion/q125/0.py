df["keywords_all"] = df.apply(lambda row: "-".join(row[1:].dropna().astype(str)), axis=1)

print(df)
