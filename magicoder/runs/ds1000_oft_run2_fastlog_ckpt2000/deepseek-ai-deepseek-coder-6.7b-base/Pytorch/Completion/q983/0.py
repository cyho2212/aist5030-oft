    return np.sum(A == B)

# Example usage
A = torch.randn(1000, 1)
B = torch.randn(1000, 1)
print(Count(A, B))
