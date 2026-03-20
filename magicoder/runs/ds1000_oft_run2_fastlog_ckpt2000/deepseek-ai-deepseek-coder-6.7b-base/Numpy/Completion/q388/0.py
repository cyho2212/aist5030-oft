result = a.reshape(a.shape[0]//patch_size, patch_size, a.shape[1]//patch_size, patch_size).transpose(0,2,1,3).reshape(-1, patch_size, patch_size)
print(result)
