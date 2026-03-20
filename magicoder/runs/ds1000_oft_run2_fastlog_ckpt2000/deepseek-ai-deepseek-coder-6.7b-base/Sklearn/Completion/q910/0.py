    le = LabelEncoder()
    df['Sex'] = le.fit_transform(df['Sex'])
    return df

df = Transform(df)
