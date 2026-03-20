result = np.where((arr[n:-n] <= arr[:-2*n]) & (arr[n:-n] <= arr[2*n:]))[0] + n
print(result)
