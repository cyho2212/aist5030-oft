arr_temp = arr.copy()
mask = arr_temp < -10
mask2 = arr_temp < 15
mask3 = arr_temp >= 15
arr[mask] = 0
arr[mask3] = arr[mask3] + 5
arr[~mask2] = 30
