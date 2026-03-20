    scaler = MinMaxScaler()
    df = pd.DataFrame(a)
    df = scaler.fit_transform(df)
    return df

# Call the function
print(Transform(np_array))
