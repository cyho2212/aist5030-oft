result = x[~np.isnan(x).any(axis=1)].tolist()
print(result)
