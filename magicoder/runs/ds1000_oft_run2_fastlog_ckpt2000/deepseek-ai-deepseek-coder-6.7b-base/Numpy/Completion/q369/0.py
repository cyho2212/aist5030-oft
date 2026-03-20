result = np.all(a[:, 1:] == a[:, :-1], axis=0)
print(result)
