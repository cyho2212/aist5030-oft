result = np.pad(a, ((0, 0), (0, 0)), 'constant', constant_values=0)[low_index:high_index, low_index:high_index]
print(result)
