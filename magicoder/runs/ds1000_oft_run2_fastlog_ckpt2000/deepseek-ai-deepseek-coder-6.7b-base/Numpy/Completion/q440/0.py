X = np.zeros((4, 3))
for i in range(4):
    X[i] = np.linalg.cholesky(Y[i])
X = X.reshape(12, order='F')
print(X)
