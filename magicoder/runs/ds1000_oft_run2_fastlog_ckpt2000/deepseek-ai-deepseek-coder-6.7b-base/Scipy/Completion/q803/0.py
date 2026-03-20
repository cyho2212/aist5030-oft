result = np.zeros(5, dtype=int)
for i in range(5):
    result[i] = np.argmin(scipy.spatial.distance.cdist(data[np.where(cluster_labels == i)], [centroids[i]]))
