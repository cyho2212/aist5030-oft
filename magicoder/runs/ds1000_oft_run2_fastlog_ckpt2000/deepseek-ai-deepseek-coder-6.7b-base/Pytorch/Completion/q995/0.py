    a_cols = a.shape[1]
    b_cols = b.shape[1]
    result = torch.zeros(a.shape[0], a_cols + b_cols - 1)
    for i in range(a_cols):
        result[:, i] = a[:, i]
    for i in range(b_cols - 1):
        result[:, a_cols + i] = b[:, i + 1]
    for i in range(a_cols - 1):
        result[:, a_cols + b_cols - 2] += a[:, i + 1]
    result[:, a_cols + b_cols - 2] /= a_cols - 1
    return result

print(solve(a, b))
