result = a.reshape(a.shape[0]//patch_size, patch_size, a.shape[1]//patch_size, patch_size).swapaxes(1,2).reshape(-1, patch_size, patch_size)
print(result)
