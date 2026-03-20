b = np.zeros((len(a), a.max() + 1))
b[np.arange(len(a)), a] = 1
print(b)
