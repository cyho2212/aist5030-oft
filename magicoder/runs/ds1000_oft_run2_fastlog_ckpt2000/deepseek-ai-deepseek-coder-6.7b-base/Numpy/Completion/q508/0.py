result = A[np.any(A, axis=1)]
result = result[:, np.any(result, axis=0)]
print(result)
