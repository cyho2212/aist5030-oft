z = np.array([[elementwise_function(x[i][j], y[i][j]) for j in range(len(x[0]))] for i in range(len(x))])
print(z)
