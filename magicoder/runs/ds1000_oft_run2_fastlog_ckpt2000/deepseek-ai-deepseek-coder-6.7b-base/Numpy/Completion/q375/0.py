low = np.min(grades)
high = np.max(grades)

def ecdf(x):
  # normalize X to sum to 1
  x = x / np.sum(x)
  return np.cumsum(x)

ecdf_values = ecdf(grades)

for i in range(len(ecdf_values)):
  if ecdf_values[i] < threshold:
    low = grades[i]
    break

for i in range(len(ecdf_values)-1, -1, -1):
  if ecdf_values[i] < threshold:
    high = grades[i]
    break

print(f"The longest interval [{low}, {high}) that satisfies ECDF(x) < {threshold} for any x in [{low}, {high}) is [{low}, {high})")
