result = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        result[i, j] = np.cos(np.pi * (i + 0.5) * (j + 0.5) / N)
result = result * np.sqrt(2 / N)
