result = []
for i in range(len(df.columns)):
    for j in range(i+1, len(df.columns)):
        if df.iloc[:, i].nunique() == 1:
            if df.iloc[:, j].nunique() == 1:
                result.append(f"{df.columns[i]} {df.columns[j]} one-2-one")
            else:
                result.append(f"{df.columns[i]} {df.columns[j]} one-2-many")
        else:
            if df.iloc[:, j].nunique() == 1:
                result.append(f"{df.columns[i]} {df.columns[j]} many-2-one")
            else:
                result.append(f"{df.columns[i]} {df.columns[j]} many-2-many")

print(result)
