result = np.einsum('ij,ik->jik', X, X)
print(result.shape)
