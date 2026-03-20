result = np.pad(A, (0, length - len(A)), 'constant', constant_values=(0, 0))
print(result)
