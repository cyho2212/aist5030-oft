def ecdf(x):
  # normalize X to sum to 1
  x = x / np.sum(x)
  return np.cumsum(x)

ecdf_grades = ecdf(grades)
result = ecdf_grades(eval)
print(result)
