
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')
df = df.sort_values(by='date')

def is_overlap(row1, row2, X):
    return abs((row1['date'] - row2['date']).days) <= X

df = df.drop_duplicates(subset='date', keep='first')

for i in range(len(df)):
    for j in range(i+1, len(df)):
        if is_overlap(df.iloc[i], df.iloc[j], X):
            df = df.drop(df.index[j])

df['date'] = df['date'].dt.strftime('%d-%b-%Y')

print(df)
