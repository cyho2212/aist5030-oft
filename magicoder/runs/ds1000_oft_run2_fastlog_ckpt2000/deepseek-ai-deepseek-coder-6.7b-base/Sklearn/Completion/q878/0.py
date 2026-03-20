    # Convert features to a 2D-array
    df = pd.DataFrame(features)
    df = pd.get_dummies(df.stack()).sum(level=0)
    return df.values

# Test
features = [
    ['f1', 'f2', 'f3'],
    ['f2', 'f4', 'f5', 'f6'],
    ['f1', 'f2']
]
print(solve(features))
