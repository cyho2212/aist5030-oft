    km.fit(X)
    centers = km.cluster_centers_
    distances = np.linalg.norm(X - centers[p], axis=1)
    indices = np.argsort(distances)[:50]
    return X[indices]

# Example usage
p = 2
samples = get_samples(p, X, km)
