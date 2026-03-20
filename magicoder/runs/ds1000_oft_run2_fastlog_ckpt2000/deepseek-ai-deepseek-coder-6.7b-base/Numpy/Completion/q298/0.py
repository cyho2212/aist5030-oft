b = np.zeros((len(a), len(a)))
for i in range(len(a)):
    b[i, np.argmin(a)] = 1
    a[np.argmin(a)] = np.inf
