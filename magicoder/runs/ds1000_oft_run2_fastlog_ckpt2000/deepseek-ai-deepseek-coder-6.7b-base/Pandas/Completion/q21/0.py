
def get_category(row):
    if row['A'] == 0:
        return 'A'
    elif row['B'] == 0:
        return 'B'
    elif row['C'] == 0:
        return 'C'
    else:
        return 'D'

df['category'] = df.apply(get_category, axis=1)

print(df)
