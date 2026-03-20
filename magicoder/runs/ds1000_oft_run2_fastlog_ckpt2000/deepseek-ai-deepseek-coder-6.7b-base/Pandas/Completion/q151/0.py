result = []
for i in range(len(df.columns)):
    for j in range(i+1, len(df.columns)):
        if df.iloc[:, i].nunique() == df.iloc[:, j].nunique():
            result.append(f"{df.columns[i]} {df.columns[j]} one-to-one")
        elif df.iloc[:, i].nunique() == 1:
            result.append(f"{df.columns[i]} {df.columns[j]} one-to-many")
        elif df.iloc[:, j].nunique() == 1:
            result.append(f"{df.columns[i]} {df.columns[j]} many-to-one")
        else:
            result.append(f"{df.columns[i]} {df.columns[j]} many-to-many")

print(result)
