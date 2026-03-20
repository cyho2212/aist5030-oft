min_idx = df.idxmin()
max_idx = df.idxmax()
result = max_idx[max_idx > min_idx]
