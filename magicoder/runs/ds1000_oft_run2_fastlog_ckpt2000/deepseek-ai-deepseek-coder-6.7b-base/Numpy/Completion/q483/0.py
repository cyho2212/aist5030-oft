x_matrix = np.array([[i**j for j in range(degree+1)] for i in x])
coefficients = np.linalg.inv(x_matrix.T @ x_matrix) @ x_matrix.T @ y
result = coefficients[::-1]
print(result)
