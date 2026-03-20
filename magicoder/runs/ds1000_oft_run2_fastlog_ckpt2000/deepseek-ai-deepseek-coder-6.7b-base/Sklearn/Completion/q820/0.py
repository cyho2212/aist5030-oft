    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df

print(solve(data))
