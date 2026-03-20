result = []
for i in range(arr.shape[0]):
    for j in range(n, arr.shape[1]-n):
        if np.all(arr[i, j-n:j+n+1] <= arr[i, j]) or np.all(arr[i, j-n:j+n+1] >= arr[i, j]):
            result.append([i, j])
print(result)
