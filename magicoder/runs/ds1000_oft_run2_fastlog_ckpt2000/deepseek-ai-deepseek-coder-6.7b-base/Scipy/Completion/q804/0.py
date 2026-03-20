result = []
for i in range(len(centroids)):
    distances = scipy.spatial.distance.cdist(data, [centroids[i]])
    closest_index = np.argmin(distances)
    result.append(data[closest_index])
