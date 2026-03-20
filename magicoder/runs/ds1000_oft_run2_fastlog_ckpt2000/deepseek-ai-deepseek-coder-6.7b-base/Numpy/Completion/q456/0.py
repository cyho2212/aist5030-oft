result = np.zeros((a.shape[0], a.shape[0]))
for i in range(a.shape[0]):
    for j in range(a.shape[0]):
        result[i, j] = np.linalg.norm(a[i] - a[j])
print(result)
