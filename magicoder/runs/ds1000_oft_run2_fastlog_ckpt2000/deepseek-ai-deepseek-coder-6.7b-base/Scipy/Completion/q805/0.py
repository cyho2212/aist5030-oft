result = []
for i in range(len(centroids)):
    distances = scipy.spatial.distance.cdist(data, [centroids[i]])
    sorted_indices = np.argsort(distances, axis=0)
    result.append(sorted_indices[:k, 0])
