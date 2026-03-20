median = np.median(col.data)
mode = np.argmax(np.bincount(col.data))
print(f"Median: {median}, Mode: {mode}")
