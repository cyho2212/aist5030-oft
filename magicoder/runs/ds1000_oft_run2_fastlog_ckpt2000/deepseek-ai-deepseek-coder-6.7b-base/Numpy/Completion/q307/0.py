result = np.pad(a, ((0,0), (shift[0], shift[1])), 'constant', constant_values=np.nan)
print(result)
