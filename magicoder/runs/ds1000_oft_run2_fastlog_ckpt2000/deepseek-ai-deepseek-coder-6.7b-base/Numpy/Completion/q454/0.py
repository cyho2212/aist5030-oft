result = X / np.max(np.abs(X), axis=1, keepdims=True)
print(result)
