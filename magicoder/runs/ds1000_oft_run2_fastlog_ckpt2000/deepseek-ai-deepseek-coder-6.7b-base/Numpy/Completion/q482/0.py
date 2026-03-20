x_matrix = np.array([[1, x[0], x[0]**2], [1, x[1], x[1]**2], [1, x[2], x[2]**2], [1, x[3], x[3]**2]])
y_matrix = np.array([y[0], y[1], y[2], y[3]])
result = np.linalg.inv(x_matrix.T @ x_matrix) @ x_matrix.T @ y_matrix
print(result)
