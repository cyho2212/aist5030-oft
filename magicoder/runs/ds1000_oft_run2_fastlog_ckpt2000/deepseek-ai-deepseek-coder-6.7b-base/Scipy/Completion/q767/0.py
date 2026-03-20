result = sparse.csr_matrix(np.array([np.pad(v, (0, max_vector_size - len(v)), 'constant') for v in vectors]))
print(result)
