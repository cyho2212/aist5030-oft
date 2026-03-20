result = np.einsum('ijk,kl->ijl', A, B)
print(result.shape)
