a = a[:, ~np.isnan(a).any(axis=0)]
print(a)
